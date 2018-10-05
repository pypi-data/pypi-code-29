## Copyright (c) 2016-2017, Blake C. Rawlings.
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
import os
import pprint
import shutil

import pkg_resources

from . import ast
from . import plugins
from . import st
from . import utils

logger = utils.logging.getLogger(__name__)

## Convenience functions.
ONE_OR_MORE = 'ONE_OR_MORE'
ONE_AND_ONLY_ONE = 'ONE_AND_ONLY_ONE'
ONE_AT_MOST = 'ONE_AT_MOST'

## FSM-related nodes.
TRANS = 'TRANS'
DEFINE = 'DEFINE'
INVAR = 'INVAR'
CTRBL = 'CTRBL'
VAR = 'VAR'
IVAR = 'IVAR'
NEXT = 'next'
INIT = 'init'

## Expressions.
CASE = 'CASE'

## Typed assignment operators.
ASSIGN_VALUE = '{}_{}'.format(ast.ASSIGN, ast.VALUE)
ASSIGN_NUMERIC = '{}_{}'.format(ast.ASSIGN, ast.NUMERIC)
DEFINE_NUMERIC = '{}_{}'.format(DEFINE, ast.NUMERIC)
ASSIGN_INTEGER = '{}_{}'.format(ast.ASSIGN, ast.INTEGER)
DEFINE_INTEGER = '{}_{}'.format(DEFINE, ast.INTEGER)

## Typed equality comparators.
EQ_BOOLEAN = '{}{}'.format(ast.EQ, ast.BOOLEAN)
NEQ_BOOLEAN = '{}{}'.format(ast.NEQ, ast.BOOLEAN)
binary_boolean_operators = (
    ast.binary_boolean_operators + (EQ_BOOLEAN, NEQ_BOOLEAN)
)
##
EQ_NUMERIC = '{}{}'.format(ast.EQ, ast.NUMERIC)
NEQ_NUMERIC = '{}{}'.format(ast.NEQ, ast.NUMERIC)
binary_numeric_operators = (
    ast.binary_arithmetic_operators + ast.inequality_comparators
    + (EQ_NUMERIC, NEQ_NUMERIC)
)


class ConversionError(Exception):
    """Error with converting part of the AST."""
    pass


class ConflictingTypesError(Exception):
    """Error with the types in the AST."""
    pass


class Var(object):
    """The intermediate representation of a variable."""

    def __init__(self, label, version, field=None):
        assert isinstance(label, utils.six.string_types)
        assert isinstance(version, int) or version is None
        assert isinstance(field, utils.six.string_types) or field is None
        self.label = label
        self.version = version
        self.field = field

    def __repr__(self):
        return 'ir.Var({}, {}, field={})'.format(
            self.label, self.version, self.field
        )

    def __str__(self):
        if self.field is None:
            ending = ''
        else:
            ending = '.{}'.format(self.field)
        if self.version is None:
            return self.label + ending
        else:
            return '{}_{}{}'.format(self.label, self.version, ending)

    def __lt__(self, other):
        return repr(self) < repr(other)

    def __eq__(self, other):
        if isinstance(other, Var):
            return (
                self.label == other.label
                and self.version == other.version
                and self.field == other.field
            )
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.label, self.version, self.field))

    def to_dict(self):
        return {
            'label': self.label,
            'version': self.version,
            'field': self.field,
        }

    def root_var(self):
        return Var(self.label, None, field=self.field)


class Converter(object):
    """Convert an AST to intermediate representation (IR)."""

    def __init__(self, loaded_plugins):
        ## `loaded_plugins` is a list of optional plugins to apply
        ## when building the model.
        self.loaded_plugins = loaded_plugins
        ## `plugin_options` is a dict that maps plugin option names to
        ## values.
        self.plugin_options = {}
        ## `assignment_count` stores the number of times each variable
        ## has had a value assigned to it.
        ##
        ## The keys are /AST/ variables.
        self.assignment_count = {}
        ## `connections` stores the number of times a variable's value
        ## depends on another variable, i.e.,
        ## `connections[var1][var2]` is the number of times `var2`
        ## appears directly in the assignment logic for `var`.
        ##
        ## The keys are /IR/ variables.
        self.connections = {}
        ## `referenced` is the set of variables that appear directly
        ## in the assignment logic for other variables.
        ##
        ## The members are /IR/ variables.
        self.referenced = set()
        ## `assigned` is the set of variables that are assigned a
        ## value somewhere in the program.
        ##
        ## The members are /AST/ variables.
        self.assigned = set()
        ## `defined` is the set of variables that have their value
        ## defined via some assignment logic in the model.
        ##
        ## The members are /IR/ variables.
        self.defined = set()
        ## `trivial` is the set of variables that only have
        ## "assignment logic" to enforce the PLC "input scan, evaluate
        ## logic, output scan" looping behavior.
        ##
        ## The members are /IR/ variables.
        self.trivial = set()
        ## `aliases` is the set of variables that are just aliases for
        ## other variables.
        ##
        ## The members are /IR/ variables.
        self.aliases = set()
        ## `ivars` is the set of input variables in the model.
        ##
        ## The members are /IR/ variables.
        self.ivars = set()
        ## `literals` is the set of literals that appear in the
        ## model.
        ##
        ## The members are /IR/ variables.
        self.literals = set()
        ## `comparisons` stores the comparison (equality, inequality,
        ## etc.) expressions that appear in the program.
        ##
        ## The members are tuples that include the AST and the /IR/
        ## variable.
        self.comparisons = []
        ## `constants` is a dict that maps the name of a constant to its
        ## constant value (which should be a literal).
        self.constants = {}
        ## `numeric` and `boolean` expressions that are used as either
        ## numeric or boolean values.
        ##
        ## The members are AST nodes.
        self.numeric = set()
        self.boolean = set()
        self.integer = set()
        ## `intermediate_representation` is the intermediate
        ## representation of the model; `logic_ir` is the
        ## assignment/transition logic.
        self.intermediate_representation = []
        self.logic_ir = []
        ## `special_variables` is a dict that tracks various types of
        ## "special" variables, so that
        ## `special_variables[variable_type]` is the set of special
        ## variables of type `variable_type` that appear in the model;
        ## these are plugin-specific.
        ##
        ## The members are /AST/ variables.
        self.special_variables = {}
        ## `context` is a list of boolean expressions that all must
        ## evaluate to "TRUE" for the inner code to be executed (e.g.,
        ## the conditions from a sequence of nested "IF" statements).
        ##
        ## The members are /IR/ nodes.
        self.context = []
        ## `if_depth` stores the number of nested "IF" statements that
        ## are currently in effect when processing an AST node.
        ##
        ## The value should be a non-negative integer.
        self.if_depth = 0
        ## `metadata_paths` is the list of file names that contain
        ## additional metadata related to the program.
        self.metadata_paths = []
        ## `sequence` is the sequence (if one was specified) of the
        ## program; this is plugin-specific.
        self.sequence = None
        ## `abstractions` stores the abstractions that will be aplpied
        ## to simplify the model.
        self.abstractions = {}
        ## `unconditional_assignments` is the set of variables that
        ## are assigned a value without checking any conditions.
        self.unconditional_assignments = set()
        ## `coi_info` is a dict that could be used to reconstruct the
        ## cone of influence information for the model.
        self.coi_info = {}

    def convert_ast(self, tree):
        """Convert the AST `tree`.

        This can be called multiple times, e.g. once for each
        statement in the AST.

        """
        if len(tree) == 0:
            return
        if isinstance(tree, list):
            if isinstance(tree[0], list):
                for statement in tree:
                    self.convert_statement(statement)
            elif tree[0] == ast.FUNCTION_BLOCK:
                assert len(tree) == 2
                assert len(tree[1]) == 3
                for declaration_block in tree[1][1]:
                    for declaration in declaration_block:
                        self.convert_declaration(declaration)
                for statement in tree[1][2]:
                    self.convert_statement(statement)
            else:
                self.convert_statement(tree)
        else:
            raise ast.AstError('Could not traverse the AST: {0}'.format(tree))

    def convert_declaration(self, tree):
        """Convert the AST `tree` that corresponds to a single declaration."""
        if tree[0] == ast.DECL_CONST:
            self.constants[tree[1][0]] = tree[1][2]
        elif tree[0] in (
                ast.DECL_VAR,
                ast.DECL_VAR_INPUT,
                ast.DECL_VAR_OUTPUT,
                ast.DECL_VAR_IN_OUT,
                ast.DECL_VAR_TEMP,
        ):
            if tree[1][1] == ('BOOL'):
                self.mark_boolean(tree[1][0])
            elif tree[1][1] in ('INT', 'DINT'):
                self.mark_integer(tree[1][0])
            elif tree[1][1] in ('REAL', 'LREAL'):
                self.mark_numeric(tree[1][0])
            else:
                raise ConversionError('Unrecognized type: {0}'.format(tree))
        else:
            raise ConversionError(
                'Unrecognized declaration: {0}'.format(tree)
            )

    def convert_statement(self, tree):
        """Convert the AST `tree` that corresponds to a single statement."""
        if tree[0] == ast.JUNK:
            return
        elif tree[0] == ast.ASSIGN:
            self._convert_assignment(tree)
        elif tree[0] == ast.IF:
            self._convert_ifelse(tree)
        elif tree[0] in (ast.CALL, ast.FUNCTION_BLOCK_CALL):
            self._convert_instruction(tree)
        else:
            raise ConversionError(
                'Unrecognized statement: {0}'.format(tree)
            )

    def _convert_ifelse(self, tree):
        """Convert an IF...ELSE statement.

        This modifies `self`.

        """
        ## Check the structure of the tree and break it up.
        assert len(tree) == 2
        assert len(tree[1]) == 3
        cond = self.convert_expression(tree[1][0])
        if_branch = tree[1][1]
        else_branch = tree[1][2]

        ## Handle the IF branch.
        self.context.append(cond)
        self.if_depth += 1
        self.convert_ast(if_branch)

        ## Handle the ELSE branch.
        self.context[self.if_depth-1] = [
            ast.NOT,
            [self.context[self.if_depth-1]]
        ]
        self.convert_ast(else_branch)
        self.context = self.context[:-1]
        self.if_depth -= 1

        ## Clean up the context.
        if self.if_depth == 0:
            assert len(self.context) == 0

    def _convert_assignment(self, tree):
        """Convert an assignment.

        This modifies `self`.

        """
        ## Get the right-hand-side expression.  If it isn't handled
        ## correctly, just mark the left-hand-side variable as being
        ## modified.
        try:
            rhs = self.convert_expression(tree[1][1])
        except ConversionError:
            logger.warning(
                'Could not convert the right-hand side, '
                'marking left-hand side as modified: {}'
                .format(tree)
            )
            self.convert_statement([ast.CALL, ['MODIFY', [tree[1][0]]]])
            return
        if self.if_depth > 0:
            ## This has to be before `lhs` is computed, because doing
            ## so increments the assignment count.
            lhs_old = self.convert_expression(tree[1][0], lhs=False)
        ## Add context/guards if necessary.
        if self.if_depth > 0:
            ## This assignment shows up under one or more IF/ELSE
            ## clauses, so it should be assigned a conditional value.
            assign_cond = self._conjoin(self.context)
            skip_cond = ast.TRUE
            rhs_with_context = [
                CASE,
                [
                    [assign_cond, rhs],
                    [skip_cond, lhs_old]
                ]
            ]
            ## Get the left-hand-side expression.
            lhs = self.convert_expression(tree[1][0], lhs=True)
        else:
            ## Not part of any IF/ELSE block, i.e., an unconditional
            ## assignment.
            lhs = self.convert_expression(tree[1][0], lhs=True)
            self.unconditional_assignments.add(lhs)
            rhs_with_context = rhs
        ## Select how to decide the assignment type.
        ## Use the new `get_type` and `set_type` methods.
        branch_types = [
            self.get_type(lhs), self.get_type(rhs_with_context)
        ]
        if ast.BOOLEAN in branch_types:
            assert set(branch_types) <= {ast.BOOLEAN, ast.VALUE}
            assignment_type = ast.BOOLEAN
        elif ast.INTEGER in branch_types:
            assert set(branch_types) <= {ast.INTEGER, ast.NUMERIC, ast.VALUE}
            assignment_type = ast.INTEGER
        elif ast.NUMERIC in branch_types:
            assert set(branch_types) <= {ast.NUMERIC, ast.VALUE}
            assignment_type = ast.NUMERIC
        else:
            assert all([x == ast.VALUE for x in branch_types])
            assignment_type = ast.VALUE
        if assignment_type != ast.VALUE:
            self.set_type(lhs, assignment_type)
            self.set_type(rhs_with_context, assignment_type)
        ## Create the assignment logic.
        self.defined.add(lhs)
        if assignment_type == ast.BOOLEAN:
            self.logic_ir.append([ast.ASSIGN, [lhs, rhs_with_context]])
        elif assignment_type == ast.INTEGER:
            self.logic_ir.append([ASSIGN_INTEGER, [lhs, rhs_with_context]])
        elif assignment_type == ast.NUMERIC:
            self.logic_ir.append([ASSIGN_NUMERIC, [lhs, rhs_with_context]])
        else:
            assert assignment_type == ast.VALUE
            self.logic_ir.append([ASSIGN_VALUE, [lhs, rhs_with_context]])
        ## Keep track of which variables influence each other.
        variables = set.union(self.defined, self.referenced)
        rhs_symbols = get_variables(rhs_with_context)
        rhs_vars = {x for x in variables if x in rhs_symbols}
        for v in rhs_vars:
            self.mark_connection(lhs, v)

    def _convert_comment(self, tree):
        """Convert a comment."""
        raise NotImplementedError(
            'Comments should have been stripped from the AST.'
        )

    def _convert_instruction(self, tree):
        """Convert an instruction.

        This modifies `self`.

        """
        call_type = tree[0]
        procedure = tree[1][0]
        arguments = tree[1][1]
        if procedure == 'MODIFY':
            assert len(arguments) == 1
            utils.try_incr(self.assignment_count, Var(arguments[0], None), 1)
        else:
            logger.warning('Unrecognized instruction: {}'.format(tree))

    def convert_expression(self, tree, lhs=False):
        """Convert the AST `tree` that corresponds to an expression.

        This modifies `self` and returns the converted expression.

        """
        ## Base cases.
        if len(tree) == 0:
            return None
        elif isinstance(tree, utils.six.string_types):
            return self._convert_variable(tree, lhs=lhs)
        else:
            assert isinstance(tree, list)

        ## Check if any plugins handle the expression.
        active_plugins = plugins.actions.get_active_plugins(
            self.loaded_plugins, plugins.actions.SPECIAL_EXPRESSIONS
        )
        for plugin in active_plugins:
            if tree[0] in plugin.SPECIAL_EXPRESSION_TYPES:
                return plugin.convert_expression(self, tree, lhs=lhs)

        ## Left-hand side variables should have been handled by now.
        assert lhs is False

        ## Recursive cases.
        if len(tree) == 1:
            return [self.convert_expression(tree[0])]
        elif tree[0] in (ast.BOOLEAN, ast.NUMERIC):
            assert len(tree) == 2
            return self._convert_literal(tree)
        elif tree[0] in (ast.CALL, ast.FUNCTION_BLOCK_CALL):
            assert len(tree) == 2
            assert len(tree[1]) == 2
            return self.convert_expression(tree[1])
        elif tree[0] in ast.boolean_operators:
            return self._convert_boolean_expression(tree)
        elif tree[0] in ast.comparators:
            return self._convert_comparison(tree)
        elif tree[0] in (ast.arithmetic_operators + ('ABS', 'POS')):
            return self._convert_numeric_expression(tree)
        else:
            raise ConversionError(
                'Unrecognized expression: {0}'.format(tree)
            )

    def _convert_variable(self, tree, lhs=False, force_version=None):
        """Convert a variable (or a literal)."""
        assert isinstance(tree, utils.six.string_types)
        if not lhs:
            utils.try_incr(self.assignment_count, Var(tree, None), 0)
        else:
            utils.try_incr(self.assignment_count, Var(tree, None), 1)
        ## Return the correct "version" of the variable.
        if force_version is None:
            version = self.assignment_count[Var(tree, None)]
        else:
            assert isinstance(force_version, int)
            version = force_version
        retval = Var(tree, version)
        ## Mark this variable's behavior/function.
        if not lhs:
            self.referenced.add(retval)
        else:
            self.assigned.add(Var(tree, None))
        ##
        return retval

    def _convert_literal(self, tree):
        """Convert a literal."""
        if tree[0] == ast.BOOLEAN:
            literal = tree[1].upper()
            assert literal in (ast.TRUE, ast.FALSE)
            self.mark_boolean(literal)
        else: # TODO: integer
            assert tree[0] == ast.NUMERIC
            literal = tree[1]
            self.mark_numeric(literal)
        self.literals.add(literal)
        retval = [tree[0], literal]
        return retval

    def _convert_boolean_expression(self, tree):
        """Convert a boolean expression."""
        assert tree[0] in ast.boolean_operators
        assert len(tree) == 2
        if tree[0] in ast.unary_boolean_operators:
            assert len(tree[1]) == 1
            self.mark_boolean(tree[1][0])
            operand = self.convert_expression(tree[1][0])
            self.set_type(operand, ast.BOOLEAN)
            return [tree[0], [operand]]
        elif tree[0] in ast.binary_boolean_operators:
            assert len(tree[1]) == 2
            self.mark_boolean(tree[1][0])
            self.mark_boolean(tree[1][1])
            operands = [self.convert_expression(x) for x in tree[1]]
            for operand in operands:
                self.set_type(operand, ast.BOOLEAN)
            return [
                tree[0],
                operands
            ]

    def _convert_comparison(self, tree):
        """Convert a numeric (in)equality comparison."""
        assert tree[0] in ast.comparators
        assert len(tree) == 2
        assert isinstance(tree[1], (tuple, list))
        assert len(tree[1]) == 2
        ##
        if tree[0] in ast.inequality_comparators:
            self.mark_numeric(tree[1][0])
            self.mark_numeric(tree[1][1])
        retval = [
            tree[0],
            [self.convert_expression(x) for x in tree[1]]
        ]
        ## Mark the comparison.
        self.mark_comparison(tree, retval)
        ##
        return retval

    def _convert_numeric_expression(self, tree):
        """Convert a numeric expression."""
        assert tree[0] in (ast.arithmetic_operators + ('ABS', 'POS'))
        assert len(tree) == 2
        assert isinstance(tree[1], (tuple, list))
        ##
        if tree[0] in (ast.unary_arithmetic_operators + ('ABS', 'POS')):
            assert len(tree[1]) == 1
            self.mark_numeric(tree[1][0])
            return [
                tree[0],
                [self.convert_expression(tree[1][0])]
            ]
        else:
            assert tree[0] in ast.binary_arithmetic_operators
            assert len(tree[1]) == 2
            self.mark_numeric(tree[1][0])
            self.mark_numeric(tree[1][1])
            return [
                tree[0],
                [self.convert_expression(x) for x in tree[1]]
            ]

    def mark_connection(self, lhs, rhs):
        """Mark a connection, where `rhs` influences `lhs`."""
        assert isinstance(lhs, Var)
        assert isinstance(rhs, Var)
        if lhs not in self.connections:
            self.connections[lhs] = {}
        utils.try_incr(self.connections[lhs], rhs, 1)

    def mark_numeric(self, tree):
        """Try to mark the AST `tree` as numeric."""
        try:
            if tree in self.boolean:
                raise ConflictingTypesError(
                    'Tried to mark `{}` as numeric, '
                    'but it is already marked as Boolean.'
                    .format(tree)
                )
            if tree in self.integer:
                logger.debug(
                    'Not weakening type of `{}` from integer to numeric.'
                    .format(tree)
                )
                return
            self.numeric.add(tree)
        except TypeError:
            pass

    def mark_integer(self, tree):
        """Try to mark the AST `tree` as an integer."""
        try:
            if tree in self.boolean:
                raise ConflictingTypesError(
                    'Tried to mark `{}` as integer, '
                    'but it is already marked as Boolean.'
                    .format(tree)
                )
            if  tree in self.numeric:
                logger.debug(
                    'Strengthening type of `{}` from numeric to integer.'
                    .format(tree)
                )
                self.numeric.remove(tree)
            self.integer.add(tree)
        except TypeError:
            pass

    def mark_boolean(self, tree):
        """Try to mark `tree` as Boolean."""
        try:
            if tree in (self.numeric | self.integer):
                raise ConflictingTypesError(
                    'Tried to mark `{}` as Boolean, '
                    'but it is already marked as {}.'
                    .format(tree, self.get_type(tree))
                )
            self.boolean.add(tree)
        except TypeError:
            pass

    def is_boolean(self, tree):
        """Check if `tree` is marked as Bolean."""
        try:
            return str(tree) in self.boolean
        except TypeError:
            return False

    def is_integer(self, tree):
        """Check if `tree` is marked as integer."""
        try:
            return str(tree) in self.integer
        except TypeError:
            return False

    def is_numeric(self, tree):
        """Check if `tree` is marked as numeric."""
        try:
            return str(tree) in self.numeric
        except TypeError:
            return False

    def mark_comparison(self, ast_tree, ir_tree):
        """Mark the AST `tree` as a comparison.

        This actually stores a modified copy of `tree` that contains
        the current versions of the variables at this point in the
        code.  The translated IR `code` (variable name) is also
        stored along with the comparison to make adding constraints
        easier later.

        """
        substituted_ast_tree = copy.deepcopy(ast_tree)
        self._replace_variables(substituted_ast_tree)
        self.comparisons.append((substituted_ast_tree, ir_tree))

    def _replace_variables(self, tree):
        """Replace the values in `tree` with their current versions.

        N.B.: this modifies `tree` in place!  It does not affect any
        other variables though (i.e., `self` is not modified).

        """
        for i in range(len(tree)):
            if tree == st.parse_symbol(
                    tree, 'bn'
            ):
                tree[i] = self._convert_literal(tree[i])
            elif tree[i] == st.parse_symbol(tree[i], 'i'):
                try:
                    tree[i] = '{0}_{1}'.format(
                        tree[i],
                        self.assignment_count[Var(tree[i], None)]
                    )
                except KeyError:
                    ## Probably a keyword/function (e.g., "ABS").
                    pass
            elif isinstance(tree[i], list):
                self._replace_variables(tree[i])

    def _conjoin(self, expressions, top_level_call=True):
        """Returns the conjunction of a list of IR `expressions`."""
        expressions = copy.deepcopy(expressions)
        if top_level_call:
            for expression in expressions:
                self.set_type(expression, ast.BOOLEAN)
        if len(expressions) == 1:
            retval = (expressions[0])
        else:
            assert len(expressions) > 1
            retval = [
                ast.AND,
                [
                    (expressions[0]),
                    self._conjoin(expressions[1:], top_level_call=False)
                ]
            ]
        return retval

    def generate_model(self):
        """Produce the intermediate representation (IR) for the model.

        After all the statements in an AST have been processed, this
        method does some final processing and generates the output
        model (as IR).  The "final processing" includes defining
        aliases for some of the variables, enforcing the "input scan,
        evaluate logic, output scan" operation of a PLC, checking for
        infeasible readings/predicates, computing abstractions to
        simplify the output model, creating and writing
        process-independent tests (PITs) for the model, and more.

        """
        tree = []

        tree += self.logic_ir

        tree += self._generate_variable_aliases()

        ## Creating the transition logic may add transition
        ## restrictions to variables (the _0 versions of them) that
        ## were previously unrestricted; keep track of this.
        (newir, trivial) = self.generate_transition_logic()
        tree += newir
        self.trivial = set.union(self.trivial, trivial)

        ## Plugins.
        active_plugins = plugins.actions.get_active_plugins(
            self.loaded_plugins, plugins.actions.TRANSITION_LOGIC
        )
        for plugin in active_plugins:
            (newir, trivial) = plugin.generate_transition_logic(self)
            tree += newir
            self.trivial = set.union(self.trivial, trivial)
            logger.debug(
                'Added transition logic from the "{}" plugin.'
                .format(plugin.NAME)
            )

        ## Metadata.
        for mp in self.metadata_paths:
            newir = self.generate_metadata_constraints(mp)
            tree += newir

        ## This has to come after any modifications to `self.trivial`.
        tree = self._generate_variable_declarations() + tree

        ## Refinements (this may modify `self.connections`, so do it
        ## before computing abstractions).
        active_plugins = plugins.actions.get_active_plugins(
            self.loaded_plugins, plugins.actions.REFINEMENT
        )
        for plugin in active_plugins:
            (constraints, connections) = plugin.compute_refinements(self)
            for connection in connections:
                self.mark_connection(connection[0], connection[1])
                self.mark_connection(connection[1], connection[0])
            tree += constraints

        ## Abstractions.
        active_plugins = plugins.actions.get_active_plugins(
            self.loaded_plugins, plugins.actions.ABSTRACTION
        )
        if len(active_plugins) > 0:
            assert len(active_plugins) == 1
            if False:
                abstractions = active_plugins[0].compute_abstractions(self)
                assert abstractions[0] not in self.abstractions
                self.abstractions[abstractions[0]] = abstractions[1]
            ## Also save the COI info.
            self.coi_info = active_plugins[0].get_coi_info(self)

        ## Store the intermediate representation.
        self.intermediate_representation = tree

    def _generate_variable_declarations(self):
        """Generate "VAR" declarations as necessary.

        This modifies `self`, and returns the new variable
        declarations.

        """
        tree = []
        readings = sorted(
            self.referenced - self.literals - self.defined - self.trivial
        )
        assert all([isinstance(x, Var) for x in readings])
        for var in readings:
            ivar = Var('ivar_{}'.format(var.label), var.version)
            self.ivars.add(ivar)
            var_type = self.get_type(var)
            if var_type == ast.BOOLEAN:
                keyword = ast.ASSIGN
            elif var_type == ast.INTEGER:
                keyword = ASSIGN_INTEGER
            elif var_type == ast.NUMERIC:
                keyword = ASSIGN_NUMERIC
            else:
                assert var_type == ast.VALUE
                keyword = ASSIGN_VALUE
            tree += [
                [IVAR, ivar, var_type],
                [VAR, var, var_type],
                [keyword, [[NEXT, var], ivar]],
            ]
            self.mark_connection(var, ivar)
        return tree

    def _generate_variable_aliases(self):
        """Define some useful variable aliases.

        This modifies `self`, and returns the new aliases.

        """
        tree = []
        for var in sorted(self.assigned):
            assert isinstance(var, Var)
            assert var.version is None
            ## Define the base variable name to refer to the final
            ## modified value.
            if 'steps' in self.special_variables:
                if var in self.special_variables['steps']:
                    ## Special case, handled elsewhere.
                    continue
            if var == 'dt':
                ## Don't track the timer variables.
                continue
            version = Var(
                var.label, self.assignment_count[var], field=var.field
            )
            if self.is_boolean(var):
                tree.append([DEFINE, [var, version]])
            elif self.is_integer(var):
                tree.append([DEFINE_INTEGER, [var, version]])
            elif self.is_numeric(var):
                tree.append([DEFINE_NUMERIC, [var, version]])
            else:
                ## The variable type is not known, skip it.
                continue
            self.aliases.add(var)
            self.mark_connection(var, version)
        return tree

    def generate_transition_logic(self):
        """Enforce the variable transition logic.

        This modifies `self`, and returns the new transition logic.

        """
        tree = []
        trivial = set()
        for var in sorted(self.assigned):
            assert isinstance(var, Var)
            assert var.version is None
            ## Check if this variable should be handled by one of the
            ## plugins.
            skip = False
            for plugin in plugins.actions.get_active_plugins(
                    self.loaded_plugins, plugins.actions.TRANSITION_LOGIC
            ):
                if plugin.has_special_transition_logic(self, var):
                    skip = True
                    break
            if skip:
                continue
            ##
            var0 = Var(var.label, 0, field=var.field)
            if var0 in self.referenced:
                self.mark_connection(var0, var)
                if self.is_boolean(var):
                    tree.append([ast.ASSIGN, [[NEXT, var0], var]])
                elif self.is_integer(var):
                    tree.append([ASSIGN_INTEGER, [[NEXT, var0], var]])
                elif self.is_numeric(var):
                    tree.append([ASSIGN_NUMERIC, [[NEXT, var0], var]])
                if var0 not in self.defined:
                    trivial.add(var0)
        return (tree, trivial)

    def generate_metadata_constraints(self, metadata_path):
        """Generate constraints on the model from some metadata.

        This reads a (JSON) file from `metadata_path` that defines
        some additional information about the system, and applies the
        corresponding constraints to the model.

        """
        ## Setup.
        tree = []
        if metadata_path == '':
            return tree
        ## Plugins.
        for plugin in plugins.actions.get_active_plugins(
                self.loaded_plugins, plugins.actions.METADATA_CONSTRAINTS
        ):
            new_ir = plugin.generate_metadata_constraints(
                self, metadata_path
            )
            tree += new_ir
        ##
        return tree

    def is_untouchable(self, variable):
        """Return whether or not `variable` is "untouchable".

        A variable is "untouchable" if it cannot (or should not) be
        abstracted away when simplifying the model.

        """
        return bool(variable in self.trivial)

    def get_type(self, tree):
        """Try to determine the type of the IR expression `tree`.

        This uses information from the nodes that appear in `tree`,
        along with variable type information that is already known.

        """
        if isinstance(tree, utils.six.string_types):
            if tree in self.literals:
                if self.is_boolean(tree):
                    return ast.BOOLEAN
                elif self.is_numeric(tree):
                    return ast.NUMERIC
                else:
                    return ast.VALUE
            else:
                print(tree)
                assert False # TODO: make sure that this is unreachable
        elif isinstance(tree, Var):
            if self.is_boolean(str(tree.root_var())):
                return ast.BOOLEAN
            elif self.is_integer(str(tree.root_var())):
                return ast.INTEGER
            elif self.is_numeric(str(tree.root_var())):
                return ast.NUMERIC
            else:
                return ast.VALUE
        elif isinstance(tree, (tuple, list)):
            assert len(tree) > 0
            if tree[0] in ast.unary_arithmetic_operators + ('ABS', 'POS'):
                return self.get_type(tree[1][0])
            if tree[0] in ast.binary_arithmetic_operators:
                operand_types = {self.get_type(x) for x in tree[1]}
                assert operand_types <= {ast.INTEGER, ast.NUMERIC}
                if ast.INTEGER in operand_types:
                    return ast.INTEGER
                else:
                    return ast.NUMERIC
            elif tree[0] in ast.boolean_operators + ast.comparators:
                return ast.BOOLEAN
            elif tree[0] == CASE:
                assert len(tree) == 2
                assert len(tree[1]) > 0
                case_types = [
                    self.get_type(x[1])
                    for x in tree[1]
                ]
                if ast.BOOLEAN in case_types:
                    assert set(case_types) <= {ast.BOOLEAN, ast.VALUE}
                    return ast.BOOLEAN
                elif ast.INTEGER in case_types:
                    assert set(case_types) <= {
                        ast.INTEGER,
                        ast.NUMERIC,
                        ast.VALUE,
                    }
                    return ast.INTEGER
                elif ast.NUMERIC in case_types:
                    assert set(case_types) <= {ast.NUMERIC, ast.VALUE}
                    return ast.NUMERIC
                else:
                    assert all([x == ast.VALUE for x in case_types])
                    return ast.VALUE
                ## TODO: propagate types, make sure the conditionals
                ## are Boolean?
            elif tree[0] in (ast.BOOLEAN, ast.NUMERIC):
                assert tree[1] in self.literals
                return self.get_type(tree[1]) # TODO: integer
            else:
                print(tree)
                assert False
        else:
            print(tree)
            assert False

    def set_type(self, tree, new_type):
        """Try to set the type of the IR expression `tree` to `new_type`.

        This moves through `tree` and calls itself recursively to set
        as many variables as possible (correctly) to `new_type`.

        """
        assert new_type in (ast.BOOLEAN, ast.INTEGER, ast.NUMERIC, ast.VALUE)
        ##
        old_type = self.get_type(tree)
        if new_type == ast.VALUE:
            assert old_type == ast.VALUE
            return
        else:
            if new_type == ast.INTEGER:
                assert old_type in (new_type, ast.NUMERIC, ast.VALUE)
            else:
                assert old_type in (new_type, ast.VALUE)
            if  new_type == ast.BOOLEAN:
                mark_type = self.mark_boolean
            elif new_type == ast.INTEGER:
                mark_type = self.mark_integer
            elif new_type == ast.NUMERIC:
                mark_type = self.mark_numeric
            else:
                assert False
        ##
        if isinstance(tree, utils.six.string_types):
            assert tree in self.literals
            assert new_type in {ast.BOOLEAN, ast.NUMERIC}
            mark_type(tree)
        elif isinstance(tree, Var):
            mark_type(str(tree.root_var()))
        elif isinstance(tree, (tuple, list)):
            assert len(tree) > 0
            dead_ends = (ast.comparators + ast.boolean_operators)
            if tree[0] in dead_ends:
                ## Nothing to do, the types should already be correct.
                return
            elif tree[0] in (ast.unary_arithmetic_operators + ('ABS', 'POS')):
                assert len(tree) == 2
                assert len(tree[1]) == 1
                self.set_type(tree[1][0], new_type)
            elif tree[0] in ast.binary_arithmetic_operators:
                assert len(tree) == 2
                assert len(tree[1]) == 2
                for operand in tree[1]:
                    self.set_type(operand, new_type)
            elif tree[0] == CASE:
                assert len(tree) == 2
                assert len(tree[1]) > 0
                for x in tree[1]:
                    self.set_type(x[1], new_type)
                ## TODO: set all the conditionals to Boolean?
            elif tree[0] in (ast.BOOLEAN, ast.NUMERIC):
                assert tree[1] in self.literals
                if new_type in {ast.INTEGER}:
                    literal_type = ast.NUMERIC
                else:
                    assert new_type in {ast.BOOLEAN, ast.NUMERIC}
                    literal_type = new_type
                self.set_type(tree[1], literal_type)
            else:
                print(tree)
                assert False
        else:
            print(tree)
            assert False

    def infer_types(self):
        """Apply type inference to add type information to the IR."""
        inferrers = []
        propagate_rules = []
        ## Assignments.
        inferrers.append(
            (
                lambda x: x == ASSIGN_VALUE,
                lambda _: ast.ASSIGN,
                lambda _: ASSIGN_INTEGER,
                lambda _: ASSIGN_NUMERIC,
            )
        )
        ## Numeric assignments (possibly integer).
        inferrers.append(
            (
                lambda x: x == ASSIGN_NUMERIC,
                lambda _: ast.ASSIGN, # `set_type` should fail in `add_types...`
                lambda _: ASSIGN_INTEGER,
                None, # already numeric
            )
        )
        ## Equality comparisons.
        inferrers.append(
            (
                lambda x: x in ast.equality_comparators,
                lambda x: '{}{}'.format(x, ast.BOOLEAN),
                lambda x: '{}{}'.format(x, ast.NUMERIC), # TODO: integer
                lambda x: '{}{}'.format(x, ast.NUMERIC),
            )
        )
        ## Propagate types through numeric operators.
        propagate_rules.append(lambda x: x in (EQ_NUMERIC,))

        ## Apply (and reapply) each of the `inferrers` until there's
        ## no change.
        hits = [
            utils.get_locations(self.logic_ir, rule=x[0])
            for x in inferrers
        ]
        n_untyped = sum([len(x) for x in hits])
        if n_untyped > 0:
            logger.debug(
                'Attempting to infer types for {} node(s).'
                .format(n_untyped)
            )
        else:
            logger.debug('Types are known for all the nodes.')
            return
        while True:
            ## Propagate types.
            while True:
                old_type_information = self._get_all_type_information()
                for rule in propagate_rules:
                    self._propagate_types(rule)
                new_type_information = self._get_all_type_information()
                if new_type_information == old_type_information:
                    break
            ## Apply each inferrer.
            for inferrer in inferrers:
                self._add_types_to_untyped_nodes(
                    rule=inferrer[0],
                    on_bool=inferrer[1],
                    on_int=inferrer[2],
                    on_num=inferrer[3],
                )
            ## Find the remaining untyped nodes.
            new_hits = [
                utils.get_locations(self.logic_ir, rule=x[0])
                for x in inferrers
            ]
            ## If new type information was added, try again (the new
            ## information may propagate through the other
            ## `inferrers`).
            got_new_information = False
            for idx, locations in enumerate(new_hits):
                old_locations = hits[idx]
                if len(locations) != len(old_locations):
                    assert len(locations) < len(old_locations)
                    got_new_information = True
                    break
            if got_new_information:
                hits = new_hits
                continue
            else:
                break
        ##
        remaining_terms = []
        if any(len(x) > 0 for x in hits):
            for locations in hits:
                remaining_terms.extend(
                    utils.get_value_at_location(self.logic_ir, x[:-1])
                    for x in locations
                )
        n_rem = len(remaining_terms)
        if n_rem > 0:
            logger.debug(
                'Could not infer types for {} node(s):\n{}'
                .format(n_rem, pprint.pformat(remaining_terms))
            )
        elif n_untyped > 0:
            logger.debug(
                'Added types to all of the {} untyped node(s).'
                .format(n_untyped)
            )

    def _add_types_to_untyped_nodes(
            self,
            rule=None, on_bool=None, on_int=None, on_num=None,
    ):
        """Try to add type information to the "untyped" nodes.

        `rule` is the rule used to find the locations of untyped
        nodes, and `on_bool` and `on_num` are functions of a single
        argument which, when called with the operator of the untyped
        node as the argument, return the value that operator should be
        replaced with if it's found to be Boolean or numeric,
        respectively.

        """
        assert rule is not None
        assert (on_bool is not None or on_int is not None or on_num is not None)
        ##
        locations = utils.get_locations(
            self.logic_ir,
            rule=rule
        )
        n = len(locations)
        if n == 0:
            return
        new_typed = 0
        for location in locations:
            assert location[-1] == 0
            idx = location[:-1]
            tree = utils.get_value_at_location(self.logic_ir, idx)
            logger.debug('Inferring the type of {}.'.format(tree))
            lhs_type = self.get_type(tree[1][0])
            rhs_type = self.get_type(tree[1][1])
            boolean = (lhs_type == ast.BOOLEAN) or (rhs_type == ast.BOOLEAN)
            integer = (ast.INTEGER in (lhs_type, rhs_type))
            numeric = (lhs_type == ast.NUMERIC) or (rhs_type == ast.NUMERIC)
            assert not (boolean and (integer or numeric))
            if boolean and on_bool is not None:
                logger.debug('The inferred type is {}.'.format(ast.BOOLEAN))
                self.set_type(tree[1][0], ast.BOOLEAN)
                self.set_type(tree[1][1], ast.BOOLEAN)
                utils.set_value_at_location(
                    self.logic_ir, location,
                    on_bool(tree[0])
                )
                new_typed += 1
            elif integer and on_int is not None:
                logger.debug('The inferred type is {}.'.format(ast.INTEGER))
                self.set_type(tree[1][0], ast.INTEGER)
                self.set_type(tree[1][1], ast.INTEGER)
                utils.set_value_at_location(
                    self.logic_ir, location,
                    on_int(tree[0])
                )
                new_typed += 1
            elif numeric and on_num is not None:
                logger.debug('The inferred type is {}.'.format(ast.NUMERIC))
                self.set_type(tree[1][0], ast.NUMERIC)
                self.set_type(tree[1][1], ast.NUMERIC)
                utils.set_value_at_location(
                    self.logic_ir, location,
                    on_num(tree[0])
                )
                new_typed += 1
            else:
                logger.debug('Could not infer the type.')
        if new_typed > 0:
            if n > 0:
                self._add_types_to_untyped_nodes(
                    rule=rule, on_bool=on_bool, on_num=on_num
                )

    def _propagate_types(self, rule):
        """Propagate type information through operators that match `rule`."""
        assert rule is not None
        locations = utils.get_locations(self.logic_ir, rule=rule)
        n = len(locations)
        if n == 0:
            return
        for location in locations:
            assert location[-1] == 0 # an operator
            idx = location[:-1] # get the tree with the operator at position 0
            tree = utils.get_value_at_location(self.logic_ir, idx)
            logger.debug('Propagating types in {}.'.format(tree))
            operand_types = {self.get_type(x) for x in tree[1]}
            logger.debug('Operand types: {}.'.format(operand_types))
            boolean = ast.BOOLEAN in operand_types
            integer = ast.INTEGER in operand_types
            numeric = ast.NUMERIC in operand_types
            if len(operand_types) <= 1:
                logger.debug('No new type information to propagate.')
            else:
                assert not (boolean and (integer or numeric))
                if boolean:
                    for operand in tree[1]:
                        self.set_type(operand, ast.BOOLEAN)
                elif integer:
                    for operand in tree[1]:
                        self.set_type(operand, ast.INTEGER)
                elif numeric:
                    for operand in tree[1]:
                        self.set_type(operand, ast.NUMERIC)
                else:
                    logger.debug('Did not propagate types.')

    def _get_all_type_information(self):
        """Get (a copy of) all the known type information.

        This should return different values before and after new type
        information is discovered.

        """
        return (
            set(self.boolean),
            set(self.integer),
            set(self.numeric),
        )

    def check_smv_variables(self):
        """Check for some expected behavior."""
        def check_vars(s):
            assert all([isinstance(x, Var) for x in s])
        def check_literals(s):
            assert all([isinstance(x, utils.six.string_types) for x in s])
        check_vars(self.referenced)
        check_vars(self.defined)
        check_vars(self.trivial)
        check_vars(self.aliases)
        check_vars(self.ivars)
        check_literals(self.literals)
        for c in self.connections:
            assert isinstance(c, Var)
            check_vars(self.connections[c])
        for c in self.comparisons:
            assert isinstance(c[1], (Var, tuple, list))


class JSONEncoder(json.JSONEncoder):
    """A custom JSON encoder that can handle the `Var` class."""

    def default(self, obj):
        if isinstance(obj, Var):
            ## Encode `obj` such that it can be decoded "losslessly",
            ## back into a `Var` object.  See `json_decode_hook` for
            ## the decoding.
            return {str(type(obj)): obj.to_dict()}
        else:
            return json.JSONEncoder.default(self, obj)


class IRWalker(object):
    """Walk an IR tree."""

    def __init__(self, tree):
        assert isinstance(tree, (tuple, list))
        self._tree = tree
        self.state_variables = set()
        self.input_variables = set()
        self.lines = []

    def walk(self):
        for chunk in self._tree:
            assert isinstance(chunk, (tuple, list))
            self.walk_statement(chunk)
        assert len(self.state_variables & self.input_variables) == 0

    def walk_statement(self, tree):
        assert isinstance(tree, (tuple, list))
        if tree[0] in (VAR, IVAR):
            assert len(tree) == 3
            self.walk_variable_declaration(tree)
        elif tree[0] in (
                ast.ASSIGN,
                ASSIGN_INTEGER, ASSIGN_NUMERIC,
                ASSIGN_VALUE,
        ):
            assert len(tree) == 2
            assert len(tree[1]) == 2
            self.walk_assignment(tree)
        elif tree[0] in (DEFINE, DEFINE_INTEGER, DEFINE_NUMERIC):
            assert len(tree) == 2
            assert len(tree[1]) == 2
            self.walk_definition(tree)
        else:
            self.walk_other_statement(tree)

    def walk_variable_declaration(self, tree):
        logger.debug('Variable declaration: {}'.format(tree))

    def walk_assignment(self, tree):
        logger.debug('Assign statement: {}'.format(tree))

    def walk_definition(self, tree):
        logger.debug('Define statement: {}'.format(tree))

    def walk_other_statement(self, tree):
        logger.error(
            'Unrecognized statement in intermediate representation: {}'
            .format(repr(tree))
        )

    def walk_expression(self, tree):
        if isinstance(tree, (Var, utils.six.string_types)):
            return self.walk_atom(tree)
        else:
            assert isinstance(tree, (tuple, list))
            assert len(tree) > 0
        if len(tree) == 1:
            return self.walk_grouping(tree)
        elif tree[0] in (ast.BOOLEAN, ast.NUMERIC):
            return self.walk_literal(tree)
        elif tree[0] in (NEXT, INIT):
            return self.walk_init_and_next(tree)
        elif tree[0] in ast.unary_boolean_operators:
            return self.walk_unop_boolean(tree)
        elif tree[0] in binary_boolean_operators:
            return self.walk_binop_boolean(tree)
        elif tree[0] in ast.unary_arithmetic_operators + ('ABS', 'POS'):
            return self.walk_unop_numeric(tree)
        elif tree[0] in binary_numeric_operators + ast.comparators:
            return self.walk_binop_numeric(tree)
        elif tree[0] == CASE:
            return self.walk_case(tree)
        elif tree[0] in (ONE_OR_MORE, ONE_AT_MOST, ONE_AND_ONLY_ONE):
            return self.walk_cardinality_expressions(tree)
        elif len(tree) > 1:
            logger.debug('Treating as a function call: {}'.format(repr(tree)))
            return self.walk_function_call(tree)
        else:
            return self.walk_other_expression(tree)

    def walk_other_expression(self, tree):
        logger.error(
            'Unrecognized expression in intermediate representation: {}'
            .format(repr(tree))
        )
        return None


def json_decode_hook(json_object):
    """JSON decoding hook to recover `Var` objects.

    Use this as the `object_hook` keyword argument of `json.load`.

    """
    if str(Var) in json_object:
        assert len(json_object) == 1
        members = json_object[str(Var)]
        return Var(members['label'], members['version'], field=members['field'])
    else:
        return json_object


def get_variables(tree):
    """Return the set of variables that appear in the IR `tree`."""
    locations = utils.get_locations(tree, rule=(lambda x: isinstance(x, Var)))
    terms = [utils.get_value_at_location(tree, l) for l in locations]
    retval = set(terms)
    return retval


def is_in_coi(tree, cone_of_influence):
    """Check if `tree` is in `cone_of_influence`."""
    locations = utils.get_locations(tree, rule=(lambda x: isinstance(x, Var)))
    terms = [utils.get_value_at_location(tree, l) for l in locations]
    variables = set(terms)
    if len(variables) == 0:
        return True
    retval = any([variable in cone_of_influence for variable in variables])
    return retval


def str2var(s, variables):
    """Try to match string `s` to one of the `Var`s in `variables`."""
    for variable in variables:
        if s == str(variable):
            return variable
    raise ValueError(s)


@utils.timing(log_fun=logger.info, log_text='Converted the ST file: {:.2f}s')
def st_to_ir(
        fname,
        metadata_paths=(),
        directory=None,
        loaded_plugins=None,
        plugin_options=None,
):
    """Convert the Structured Text file `fname` to an SMV model.

    This writes the model (and possibly other output) and returns the
    `Converter` object.

    """
    if loaded_plugins is None:
        loaded_plugins = []
    if plugin_options is None:
        plugin_options = {}

    ## Parse the input file.
    tree = st.get_ast(fname)

    ## Check for any plugins that do AST transformations, and apply
    ## them.
    for plugin in plugins.actions.get_active_plugins(
            loaded_plugins, plugins.actions.AST_TRANSORMATIONS
    ):
        transformer = plugin.Transformer()
        transformed = transformer.transform_ast(tree)
        tree = transformed
        logger.debug(
            'Applied AST transformations from the "{}" plugin.'
            .format(plugin.NAME)
        )

    ## Save the AST in `directory`.
    ast.write_ast(tree, directory=directory)

    ## Convert the AST to IR.
    conv = Converter(loaded_plugins)
    conv.metadata_paths = metadata_paths
    conv.plugin_options = plugin_options
    conv.convert_ast(tree)
    conv.infer_types()
    conv.generate_model()

    ## Run some sanity checks on the IR.
    conv.check_smv_variables()

    ## Write some output now.
    if directory is not None:
        if not os.path.isdir(directory):
            os.mkdir(directory)
    write_tests(conv, directory)
    if len(conv.abstractions) > 0:
        write_abstractions(conv, directory)
    if len(conv.coi_info) > 0:
        write_coi_info(conv, directory)
    copy_auxiliary(conv, directory)

    ## Write the output.
    path = directory + os.sep + 'model.json'
    with open(path, 'w') as f:
        json.dump(
            conv.intermediate_representation, f,
            indent=2, separators=(',', ': '),
            sort_keys=True,
            cls=JSONEncoder
        )
        f.write('\n')

    return conv


def write_tests(conv, directory):
    """Write process-independent tests (PITs) in `directory`/pits/."""

    ## Plugins.
    plugin_pits = []
    for plugin in plugins.actions.get_active_plugins(
            conv.loaded_plugins, plugins.actions.PROCESS_INDEPENDENT_TESTS
    ):
        new = plugin.generate_pits(conv)
        for old in plugin_pits:
            assert old['PIT_PREFIX'] != new['PIT_PREFIX']
        plugin_pits.append(new)

    ## Combine the tests.
    tests = {}
    pit_dicts = plugin_pits
    for pit_dict in pit_dicts:
        for key in pit_dict:
            if key == 'PIT_PREFIX':
                continue
            if key not in tests:
                tests[key] = []
            tests[key] += pit_dict[key]

    ## Write the PITs.
    pit_dir = directory + os.sep + 'pits'
    if not os.path.isdir(pit_dir):
        os.mkdir(pit_dir)
    for key in tests:
        path = pit_dir + os.sep + '{}.smv'.format(key)
        with open(path, 'w') as f:
            f.write('\n'.join(tests[key]))
            f.write('\n')

    return


def write_abstractions(conv, directory):
    """Write the abstractions in `directory`/abstractions."""
    abstractions_dir = directory + os.sep + 'abstractions'
    if not os.path.isdir(abstractions_dir):
        os.mkdir(abstractions_dir)
    for abstraction_type in conv.abstractions:
        for key in conv.abstractions[abstraction_type]:
            path = (
                abstractions_dir
                + os.sep
                + '{}-{}.json'.format(abstraction_type, key)
            )
            with open(path, 'w') as f:
                json.dump(
                    conv.abstractions[abstraction_type][key], f,
                    indent=2, separators=(',', ': '),
                    sort_keys=True,
                    cls=JSONEncoder
                )
                f.write('\n')
    return


def write_coi_info(conv, directory):
    """Write the COI info in `directory`."""
    with open(directory + os.sep + 'coi_info.json', 'w') as f:
        json.dump(
            conv.coi_info, f,
            indent=2, separators=(',', ': '),
            sort_keys=True,
            cls=JSONEncoder
        )
        f.write('\n')
    return


def copy_auxiliary(conv, directory):
    """Copy some auxiliary files (SMV modules, etc.) to `directory`."""
    aux_names = ['Makefile.run']
    if 'timers' in conv.special_variables:
        aux_names.append('delay_timer.smv')
    for aux_name in aux_names:
        aux_location = pkg_resources.resource_filename(__name__, aux_name)
        shutil.copyfile(
            aux_location,
            directory + os.sep + aux_name
        )


def get_coi_and_deleted_variables(
        metadatas, variable_strings, loaded_plugins, plugin_options
):
    """Compute the cone of influence and deleted variables."""
    initializing = Var('initializing', None)
    deleted_variables = set()
    cone_of_influence = {initializing}
    if variable_strings is None:
        ## Load the already-generated COI info.
        for metadata in metadatas:
            if os.path.exists(metadata):
                ## Check the metadata file for things like deleted nodes,
                ## etc.
                with open(metadata, 'r') as f:
                    s = f.read()
                    try:
                        j = json.loads(s, object_hook=json_decode_hook)
                    except ValueError:
                        logger.warning(
                            'Could not read JSON metadata: {}'.format(metadata)
                        )
                        j = {}
                    deleted_variables |= set(j.get('deleted', []))
                    cone_of_influence |= set(j.get('coi', []))
            else:
                if len(metadata) > 0:
                    logger.warning('Missing metadata file: {}'.format(metadata))
    else:
        try:
            ## Compute the COI info on the fly.
            active_plugins = plugins.actions.get_active_plugins(
                loaded_plugins, plugins.actions.ABSTRACTION
            )
            assert len(active_plugins) == 1
            plugin = active_plugins[0]
            (deleted, size, size0, target, coi) = plugin.get_variable_cuts(
                variable_strings, plugin_options
            )
            cone_of_influence |= coi
            deleted_variables |= deleted
        except AssertionError:
            logger.warning('Could not compute the COI info.')
            return (None, None)
    ## Do some cleanup and reporting.
    structures = set()
    for coi_var in cone_of_influence:
        if coi_var.field is not None:
            structure = copy.deepcopy(coi_var)
            structure.field = None
            structures.add(structure)
    cone_of_influence |= structures
    for var in deleted_variables:
        logger.debug('Deleting variable logic: {}'.format(var))
        assert isinstance(var, Var)
    ##
    return (cone_of_influence, deleted_variables)
