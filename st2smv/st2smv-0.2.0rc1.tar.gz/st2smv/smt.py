## Copyright (c) 2018, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import copy
import json

from . import ast
from . import ir
from . import utils

logger = utils.logging.getLogger(__name__)

## Use variables in the pySMT model to represent the initial constraints,
## invariant state invariants, and transition constraints.
_INIT = 'I'
_INVAR = 'C'
_TRANS = 'T'
## Also, record the sets of state and input variables.
_VARs = set()
_IVARs = set()


class IRWalker(ir.IRWalker):

    def __init__(self, tree):
        ir.IRWalker.__init__(self, tree)
        self.declarations = [] # variable declarations (order matters)

    def walk_variable_declaration(self, tree):
        var = tree[1]
        typ = tree[2]
        ## Track declarations.
        if tree[0] == ir.VAR:
            category = self.state_variables
        elif tree[0] == ir.IVAR:
            category = self.input_variables
        else:
            return self.walk_other_statement(tree)
        if var not in category:
            if typ in (ast.BOOLEAN, ast.INTEGER, ast.NUMERIC):
                self.declarations.append(
                    _declare_variable(
                        self.walk_expression(var),
                        typ=convert_symbol(typ),
                    )
                )
                category.add(var)
                return None
            elif typ != ast.VALUE:
                self.lines.append('{} = {}'.format(
                    self.walk_expression(var),
                    self.walk_expression(typ),
                ))
                return None
            else:
                return self.walk_other_statement(tree)
        else:
            return None

    def walk_assignment(self, tree):
        if tree[0] in (ast.ASSIGN, ir.ASSIGN_INTEGER, ir.ASSIGN_NUMERIC):
            lhs = self.walk_expression(tree[1][0])
            rhs = self.walk_expression(tree[1][1])
            ## Track declarations.
            if isinstance(tree[1][0], (tuple, list)):
                assert len(tree[1][0]) == 2
                assert tree[1][0][0] in (ir.NEXT, ir.INIT)
                lhs_var = tree[1][0][1]
            else:
                lhs_var = tree[1][0]
                assert isinstance(lhs_var, ir.Var)
            if lhs_var not in self.state_variables:
                self.state_variables.add(lhs_var)
                if tree[0] == ir.ASSIGN_NUMERIC:
                    typ = convert_symbol(ast.NUMERIC)
                elif tree[0] == ir.ASSIGN_INTEGER:
                    typ = convert_symbol(ast.INTEGER)
                else:
                    typ = convert_symbol(ast.BOOLEAN)
                self.declarations.append(_declare_variable(lhs_var, typ=typ))
            ##
            if isinstance(tree[1][0], (tuple, list)):
                if tree[1][0][0] == ir.INIT:
                    constraint_type = _INIT
                else:
                    assert tree[1][0][0] == ir.NEXT
                    constraint_type = _TRANS
            else:
                constraint_type = _INVAR
            self.lines.append(_add_constraint(
                constraint_type,
                'Equals({}, {})'.format(lhs, rhs)
            ))
        else:
            self.walk_other_statement(tree)

    def walk_definition(self, tree):
        if tree[0] in (ir.DEFINE, ir.DEFINE_INTEGER, ir.DEFINE_NUMERIC):
            lhs_var = self.walk_expression(tree[1][0])
            if tree[0] == ir.DEFINE:
                self.declarations.append(_declare_variable(lhs_var))
            elif tree[0] == ir.DEFINE_INTEGER:
                self.declarations.append(_declare_variable(
                    lhs_var,
                    convert_symbol(ast.INTEGER),
                ))
            else:
                assert tree[0] == ir.DEFINE_NUMERIC
                self.declarations.append(_declare_variable(
                    lhs_var,
                    convert_symbol(ast.NUMERIC),
                ))
            self.lines.append(_add_constraint(
                _INVAR,
                'Equals({}, {})'.format(
                    lhs_var,
                    self.walk_expression(tree[1][1])
                )
            ))
            self.state_variables.add(lhs_var)
        else:
            self.walk_other_statement(tree)

    def walk_atom(self, tree):
        try:
            return convert_symbol(tree)
        except ir.ConversionError:
            return str(tree)

    def walk_grouping(self, tree):
        return '({})'.format(self.walk_expression(tree[0]))

    def walk_literal(self, tree):
        if tree[0] == ast.BOOLEAN:
            assert tree[1] in (ast.TRUE, ast.FALSE)
            return convert_symbol(tree[1])
        elif tree[0] == ast.NUMERIC: # TODO: handle integer and real "correctly"
            if '.' in tree[1]:
                return 'Real({})'.format(tree[1])
            else:
                return 'Int({})'.format(tree[1])
        else:
            return self.walk_other_expression

    def walk_init_and_next(self, tree):
        assert len(tree) == 2
        if tree[0] == ir.NEXT:
            return 'shift({})'.format(self.walk_expression(tree[1]))
        elif tree[0] == ir.INIT:
            return self.walk_expression(tree[1])
        else:
            return self.walk_other_expression

    def walk_unop_boolean(self, tree):
        return self._walk_unop(tree)

    def walk_binop_boolean(self, tree):
        return self._walk_binop(tree)

    def walk_unop_numeric(self, tree):
        return self._walk_unop(tree)

    def walk_binop_numeric(self, tree):
        return self._walk_binop(tree)

    def walk_case(self, tree):
        assert len(tree) == 2
        assert len(tree[1]) >= 2 # MAYBE: simplify a single-clause `case`.
        for (idx, pair) in enumerate(tree[1]):
            if idx < len(tree[1]) - 2:
                ## Not the second-to-last pair.
                remaining = copy.deepcopy(tree)
                del remaining[1][0]
                return 'Ite({}, {}, {})'.format(
                    self.walk_expression(pair[0]),
                    self.walk_expression(pair[1]),
                    self.walk_expression(remaining),
                )
            else:
                ## The second-to-last pair; assume that the case was exhaustive.
                assert idx == len(tree[1]) - 2
                return 'Ite({}, {}, {})'.format(
                    self.walk_expression(pair[0]),
                    self.walk_expression(pair[1]),
                    self.walk_expression(tree[1][idx + 1][1]),
                )

    def walk_cardinality_expressions(self, tree):
        ## TODO: test and debug this
        assert len(tree[1]) > 0
        operator = {
            ir.ONE_OR_MORE: 'Or',
            ir.ONE_AT_MOST: 'AtMostOne',
            ir.ONE_AND_ONLY_ONE: 'ExactlyOne',
        }[tree[0]]
        return '{}({})'.format(
            operator,
            ', '.join([str(self.walk_expression(x)) for x in tree[1]])
        )

    def walk_function_call(self, tree):
        ## TODO: convert to pySMT (and test and debug)
        return '{}({})'.format(
            self.walk_expression(tree[0]),
            ', '.join(
                [str(self.walk_expression(x)) for x in tree[1:]]
            )
        )

    def _walk_unop(self, tree):
        assert len(tree) == 2
        assert len(tree[1]) == 1
        return '{}({})'.format(
            convert_symbol(tree[0]),
            self.walk_expression(tree[1][0]),
        )

    def _walk_binop(self, tree):
        assert len(tree) == 2
        return '{}({}, {})'.format(
            convert_symbol(tree[0]),
            self.walk_expression(tree[1][0]),
            self.walk_expression(tree[1][1]),
        )


def convert_symbol(symbol):
    """Convert a symbol from AST/IR syntax to pySMT syntax."""
    mapping = {
        ast.AND: 'And',
        ast.OR: 'Or',
        ast.XOR: 'Xor',
        ast.NOT: 'Not',
        ast.LT: 'LT',
        ast.LEQ: 'LE',
        ast.GT: 'GT',
        ast.GEQ: 'GE',
        ast.MLT: 'Times',
        ast.SUB: 'Minus',
        ast.ADD: 'Plus',
        ast.DIV: 'Div',
        ast.NEG: 'Neg',
        'ABS': 'Abs',
        'POS': '',
        ir.EQ_BOOLEAN: 'Iff',
        ir.NEQ_BOOLEAN: 'Xor',
        ir.EQ_NUMERIC: 'Equals',
        ir.NEQ_NUMERIC: 'NotEquals',
        ast.EQ: 'EqualsOrIff',
        ast.NEQ: 'NotEqualsOrIff',
        ast.BOOLEAN: 'types.BOOL',
        ast.INTEGER: 'types.INT',
        ast.NUMERIC: 'types.REAL', # TODO: handle REAL vs INT
        ast.TRUE: 'TRUE()',
        ast.FALSE: 'FALSE()',
    }
    for key in mapping:
        if key == symbol:
            return mapping[key]
    raise ir.ConversionError('Unrecognized symbol: {0}'.format(symbol))


def ir_to_lines(tree):
    """Convert the IR `tree` to lines of pySMT code."""
    ir_walker = IRWalker(tree)
    ir_walker.walk()
    _VARs.update(ir_walker.state_variables)
    _IVARs.update(ir_walker.input_variables)
    return ir_walker.declarations + ir_walker.lines


def _declare_variable(var, typ='types.BOOL'):
    return '{0} = Symbol("{0}", {1})'.format(var, typ)


def _add_constraint(constraint_type, expression):
    return '{0} = And({0}, {1})'.format(constraint_type, expression)


def combine(infiles, metadatas, variables, loaded_plugins, plugin_options):
    """Combine multiple pySMT components to form a single model."""
    _VARs.clear()
    _IVARs.clear()
    (cone_of_influence, deleted) = ir.get_coi_and_deleted_variables(
        metadatas, variables, loaded_plugins, plugin_options
    )
    modules = []
    raw = []
    output = []
    for infile in infiles:
        with open(infile, 'r') as f:
            if infile.endswith('smv'):
                lines = f.readlines()
                if any(['MODULE' in l for l in lines]):
                    modules += lines
                else:
                    raw += lines
            else:
                ## Structured (JSON) input, easy to do the
                ## replacements.
                assert infile.endswith('json')
                statements = json.load(f, object_hook=ir.json_decode_hook)
                if variables is None or None in (cone_of_influence, deleted):
                    logger.warning(
                        'COI info is not available, '
                        'no abstractions will be applied.'
                    )
                    intermediate_representation = statements
                else:
                    intermediate_representation = []
                    for statement in statements:
                        ## Skip assignments to non-influencing variables.
                        if statement[0] in (ast.ASSIGN, ir.DEFINE):
                            ## Find out what the LHS variable is.
                            if isinstance(statement[1][0], ir.Var):
                                var = statement[1][0]
                            else:
                                assert statement[1][0][0] in (ir.INIT, ir.NEXT)
                                var = statement[1][0][1]
                            if not isinstance(var, ir.Var):
                                logger.error(
                                    'Could not determine LHS variable '
                                    'in assignment: {}'
                                    .format(statement)
                                )
                                assert False
                            ## Skip any variables that aren't in the cone
                            ## of influence.
                            if var not in cone_of_influence:
                                if var in deleted:
                                    logger.error(
                                        'Deleted variable not in COI: {}'
                                        .format(var)
                                    )
                                    assert False
                                if var.field is None:
                                    continue
                            ## Replace the `deleted` variables with dummy
                            ## inputs.
                            if var in deleted:
                                if var not in cone_of_influence:
                                    logger.error(
                                        'Deleted variable not in COI: {}'
                                        .format(var)
                                    )
                                    assert False
                                ivar = 'ivar_{}'.format(var)
                                intermediate_representation.append(
                                    (ir.IVAR, ivar, ast.BOOLEAN)
                                )
                                intermediate_representation.append(
                                    (ir.VAR, var, ast.BOOLEAN)
                                )
                                intermediate_representation.append(
                                    (ast.ASSIGN, ((ir.NEXT, var), ivar))
                                )
                                continue
                        ## Skip non-influencing statements.
                        elif not ir.is_in_coi(statement, cone_of_influence):
                            continue
                        ## At this point, we can't prove that the
                        ## statement doesn't influence the
                        ## specification, so include it in the model.
                        intermediate_representation.append(statement)
                output += ir_to_lines(intermediate_representation)
    ## Initialze some variables.
    header = ['{} = TRUE()'.format(x) for x in (_INIT, _INVAR, _TRANS)]
    ## Print the model.
    for line in header + modules + output + raw:
        print(line.strip())
    ## Define which are the state and input variables.
    print('state_variables = [{}]'.format(', '.join(sorted([
        str(x) for x in _VARs
    ]))))
    print('input_variables = [{}]'.format(', '.join(sorted([
        str(x) for x in _IVARs
    ]))))
