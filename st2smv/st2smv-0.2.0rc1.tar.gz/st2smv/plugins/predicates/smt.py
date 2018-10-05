## Copyright (c) 2015-2017, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import pprint

import pysmt.shortcuts
import pysmt.typing
import pysmt.oracles

from ... import ast
from ... import st
from ... import utils

logger = utils.logging.getLogger(__name__)

VAROPS = (ast.DISJUNCTION, ast.CONJUNCTION)
BINOPS = ast.comparators + ast.binary_arithmetic_operators
UNOPS = (ast.NEG, 'ABS', 'POS')

def is_infeasible(cw, combination):
    """Check if `combination` is infeasible, where `combination` is a dict
    that maps predicates to `True` or `False` if they should be
    satisfied or violated.

    """
    formula = _build_model(cw, combination)
    if formula is not None:

        logic = pysmt.oracles.get_logic(formula)

        logger.debug('Built the PySMT formula')

        backend = 'z3'
        backend = 'msat'
        with pysmt.shortcuts.Solver(name=backend, logic=logic) as solver:
            solver.add_assertion(formula)
            is_sat = solver.solve()
            if is_sat:
                logger.debug('SAT')
            else:
                logger.debug('UNSAT')
            return not is_sat
    else:
        ## There were unhandled terms (probably
        ## conjunction/disjunction).
        logger.warning('Could not build the PySMT formula; assuming feasible')
        return False

def _build_model(cw, combination):
    ## Get the terms.
    terms = []
    for idx in combination:
        sat = combination[idx]
        expr = cw.transformed[idx]
        if sat:
            term = _convert_expression(
                expr,
                cw.var_info,
            )
        else:
            term = _convert_expression(
                _negate(expr),
                cw.var_info,
            )
        terms.append(term)

    ## Check for unhandled terms.
    if any([term is None for term in terms]): ## pyomo overloads `==`
        return None

    return pysmt.shortcuts.And(*terms)

def _convert_expression(tree, var_info):
    """Convert a ST expression to a PySMT formula.  This modifies
    `var_info` in place if `tree` is a variable.

    """
    if isinstance(tree, utils.six.string_types):
        numval = st.parse_symbol(tree, 'n')
        if numval is not None:
            return pysmt.shortcuts.Real(float(tree))
        varname = st.parse_symbol(tree, 'i')
        if varname is not None:
            assert varname in var_info
            try:
                retval = var_info[varname]['pysmt']
            except KeyError:
                retval = pysmt.shortcuts.Symbol(varname, pysmt.typing.REAL)
                var_info[varname]['pysmt'] = retval
            return retval
        ## This should be unreachable.
        assert False
    else:
        assert tree[0] != 'ABS'
        fun = _convert_symbol(tree[0])
        if tree[0] in VAROPS + BINOPS:
            return fun(
                [_convert_expression(x, var_info) for x in tree[1]]
            )
        elif tree[0] in UNOPS:
            return fun(
                _convert_expression(tree[1], var_info),
            )
        else:
            logger.warning(tree)
            assert False

def _convert_symbol(symbol):
    """Convert a symbol from ST syntax to PySMT."""
    mapping = {
        ast.LT: lambda pair: pysmt.shortcuts.LT(pair[0], pair[1]),
        ast.LEQ: lambda pair: pysmt.shortcuts.LE(pair[0], pair[1]),
        ast.GT: lambda pair: pysmt.shortcuts.GT(pair[0], pair[1]),
        ast.GEQ: lambda pair: pysmt.shortcuts.GE(pair[0], pair[1]),
        ast.EQ: lambda pair: pysmt.shortcuts.Equals(pair[0], pair[1]),
        ast.NEQ: lambda pair: pysmt.shortcuts.Not(
            pysmt.shortcuts.Equals(pair[0], pair[1])
        ),
        ast.MLT: lambda pair: pysmt.shortcuts.Times(pair[0], pair[1]),
        ast.SUB: lambda pair: pysmt.shortcuts.Minus(pair[0], pair[1]),
        ast.ADD: lambda pair: pysmt.shortcuts.Plus(pair[0], pair[1]),
        ast.DIV: lambda pair: pysmt.shortcuts.Div(pair[0], pair[1]),
        # 'ABS': abs,
        ast.NEG: lambda x: pysmt.shortcuts.Times(pysmt.shortcuts.Real(-1.0), x),
        'POS': lambda x: x,
        ast.CONJUNCTION: lambda varargs: pysmt.shortcuts.And(*varargs),
        ast.DISJUNCTION: lambda varargs: pysmt.shortcuts.Or(*varargs),
    }
    for key in mapping:
        if key == symbol:
            return mapping[key]
    raise KeyError(
        'Symbol could not be mapped to PySMT: {0}'.format(symbol)
    )

def _negate(tree):
    """Returns the logical negation of an AST."""
    if tree is None:
        return tree
    operator = tree[0]
    mapping = {
        ast.LT: ast.GEQ,
        ast.LEQ: ast.GT,
        ast.GT: ast.LEQ,
        ast.GEQ: ast.LT,
        ast.EQ: ast.NEQ,
        ast.NEQ: ast.EQ,
        ast.CONJUNCTION: (ast.DISJUNCTION, _negate),
        ast.DISJUNCTION: (ast.CONJUNCTION, _negate),
    }
    logger.debug('Expression: {}'.format(pprint.pformat(tree)))
    if operator not in mapping:
        logger.warning('Unknown operator: {}'.format(operator))
        return tree
    negated_operator = mapping[operator]
    if isinstance(negated_operator, (tuple, list)):
        fun = negated_operator[0]
        helper = negated_operator[1]
    else:
        fun = negated_operator
        helper = lambda x: x
    negated_tree = [fun, [helper(x) for x in tree[1]]]
    logger.debug('Negation: {}'.format(pprint.pformat(negated_tree)))
    return negated_tree
