## Copyright (c) 2015-2017, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import json
import os
import subprocess

import pyparsing

from . import ast
from . import ir
from . import plugins
from . import utils

logger = utils.logging.getLogger(__name__)

NUSMV_2_6_0_KEYWORDS = (
    'MODULE', 'DEFINE', 'MDEFINE', 'CONSTANTS', 'VAR',
    'IVAR', 'FROZENVAR', 'INIT', 'TRANS', 'INVAR', 'SPEC',
    'CTLSPEC', 'LTLSPEC', 'PSLSPEC', 'COMPUTE', 'NAME',
    'INVARSPEC', 'FAIRNESS', 'JUSTICE', 'COMPASSION', 'ISA',
    'ASSIGN', 'CONSTRAINT', 'SIMPWFF', 'CTLWFF', 'LTLWFF',
    'PSLWFF', 'COMPWFF', 'IN', 'MIN', 'MAX', 'MIRROR', 'PRED',
    'PREDICATES', 'process', 'array', 'of', 'boolean', 'integer',
    'real', 'word', 'word1', 'bool', 'signed', 'unsigned',
    'extend', 'resize', 'sizeof', 'uwconst', 'swconst', 'EX',
    'AX', 'EF', 'AF', 'EG', 'AG', 'E', 'F', 'O', 'G', 'H', 'X',
    'Y', 'Z', 'A', 'U', 'S', 'V', 'T', 'BU', 'EBF', 'ABF', 'EBG',
    'ABG', 'case', 'esac', 'mod', 'next', 'init', 'union', 'in',
    'xor', 'xnor', 'self', 'TRUE', 'FALSE', 'count'
)
SYNTHSMV_KEYWORDS = ('SYNTH', 'CTRBL')
KEYWORDS = NUSMV_2_6_0_KEYWORDS + SYNTHSMV_KEYWORDS

## `_COMPARISONS` tracks Boolean variables that are created to take
## the place of numeric comparisons when converting IR to an SMV
## model.
##
## TODO: get rid of this global variable (hack).
_COMPARISONS = set()


class SolverCommunicator(object):
    """Communicate with a running SMV solver process."""

    def __init__(self, solver, arguments, model):
        """Start the solver and build the model."""
        cmd = [solver] + arguments
        if '-int' not in cmd:
            cmd.append('-int') # start the solver in "interactive" mode
        try:
            self.process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            )
        except:
            logger.error(
                'Failed to start the SMV process ({})'.format(cmd),
                exc_info=True,
            )
            self.process = None
        self.outputs = []
        self.read_stdout()
        self.write_stdin('read_model -i {}'.format(model))
        self.read_stdout()
        self.write_stdin('go')
        self.read_stdout()

    def __del__(self):
        """Stop the solver."""
        self.write_stdin('quit')

    def read_stdout(self):
        """Read the output from the solver, through the prompt for new input.

        Returns the message up to (not including) the prompt.

        """
        raw_output = ''
        prompt = 'SynthSMV > '
        while True:
            raw_output += self.process.stdout.read(1).decode()
            if raw_output.endswith(prompt):
                break
        output = raw_output[:-(1 + len(prompt))]
        self.outputs.append(output)
        return output

    def write_stdin(self, command):
        self.process.stdin.write((command + os.linesep).encode())
        self.process.stdin.flush()

    def get_path(self, target='TRUE'):
        specification = 'AG(!({}))'.format(target)
        command = 'check_ctlspec -p "{}"'.format(specification)
        self.write_stdin(command)
        result = self.read_stdout()
        assert result.startswith('-- specification AG')
        reachable = 'is false' in result.split(os.linesep)[0]
        if reachable:
            return result
        else:
            return None


class IRWalker(ir.IRWalker):

    def __init__(self, tree):
        ir.IRWalker.__init__(self, tree)
        self.comparisons = set() # uninterpreted numeric comparisons (Booleans)
        self.grouping = True # show all grouping parentheses

    def walk_variable_declaration(self, tree):
        var = tree[1]
        rhs = tree[2]
        ## Track declarations.
        if tree[0] == ir.VAR:
            category = self.state_variables
        elif tree[0] == ir.IVAR:
            category = self.input_variables
        else:
            assert False
        if var not in category:
            category.add(var)
            if rhs == ast.BOOLEAN:
                self.lines.append(
                    '{} {} : {};'.format(
                        convert_symbol(tree[0]),
                        self.walk_expression(var),
                        self.walk_expression(rhs)
                    )
                )
            else:
                logger.debug('Skipping variable declaration: {}'.format(tree))

    def walk_assignment(self, tree):
        logger.debug(tree)
        if tree[0] == ast.ASSIGN:
            assert len(tree) == 2
            assert len(tree[1]) == 2
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
            if not (isinstance(lhs_var, ir.Var) or lhs_var is None):
                print(lhs_var)
                print(type(lhs_var))
                assert False
            if isinstance(lhs_var, ir.Var):
                if lhs_var not in self.state_variables:
                    self.state_variables.add(lhs_var)
                    self.lines.append('VAR {} : {};'.format(lhs_var, 'boolean'))
            ##
            self.lines.append('ASSIGN {} := {};'.format(lhs, rhs))
        else:
            self.walk_other_statement(tree)

    def walk_definition(self, tree):
        if tree[0] == ir.DEFINE:
            self.lines.append(
                '{} {} := {};'.format(
                    tree[0],
                    self.walk_expression(tree[1][0]),
                    self.walk_expression(tree[1][1])
                )
            )
        else:
            self.walk_other_statement(tree)

    def walk_other_statement(self, tree):
        if tree[0] == 'MODULE':
            assert len(tree) == 2
            self.lines.append(
                '{} {}'.format(
                    tree[0],
                    self.walk_expression(tree[1])
                )
            )
        elif tree[0] in (ir.CTRBL, ir.INVAR, ir.TRANS):
            assert len(tree) == 2
            self.lines.append(
                '{} {};'.format(
                    tree[0],
                    self.walk_expression(tree[1])
                )
            )
        elif tree[0] == 'PIT':
            assert len(tree) == 2
            self.lines.append('\n'.join(tree[1]))
        elif tree[0] in (ir.ASSIGN_NUMERIC, ir.ASSIGN_VALUE):
            if False: # TODO: add an argument, or remove this
                self.lines.append('-- {} assignment to {}'.format(
                    ('numeric' if tree[0] == ir.ASSIGN_NUMERIC else 'untyped'),
                    self.walk_expression(tree[1][0])
                ))
        else:
            logger.debug(
                'Unrecognized statement in intermediate representation: {}'
                .format(repr(tree))
            )

    def walk_atom(self, tree):
        try:
            return convert_symbol(tree)
        except ir.ConversionError:
            return str(tree)

    def walk_grouping(self, tree):
        if self.grouping is True:
            format_string = '({})'
        else:
            format_string = '{}'
        return format_string.format(
            self.walk_expression(tree[0])
        )

    def walk_literal(self, tree):
        if tree[0] == ast.BOOLEAN:
            assert tree[1] in (ast.TRUE, ast.FALSE)
            return tree[1]
        else:
            assert tree[0] == ast.NUMERIC
            return '{}c'.format(
                tree[1]
                .replace('.', 'p')
                .replace('-', 'neg__')
                .replace('+', '')
            )

    def walk_init_and_next(self, tree):
        assert len(tree) == 2
        return '{}({})'.format(
            convert_symbol(tree[0]),
            self.walk_expression(tree[1]),
        )

    def walk_unop_boolean(self, tree):
        assert len(tree) == 2
        assert len(tree[1]) == 1
        return '({} {})'.format(
            convert_symbol(tree[0]), self.walk_expression(tree[1][0])
        )

    def walk_binop_boolean(self, tree):
        assert len(tree) == 2
        return '({} {} {})'.format(
            self.walk_expression(tree[1][0]),
            convert_symbol(tree[0]),
            self.walk_expression(tree[1][1]),
        )

    def walk_unop_numeric(self, tree):
        assert len(tree) == 2
        assert len(tree[1]) == 1
        grouping_was = self.grouping
        self.grouping = False
        rhs = self.walk_expression(tree[1][0])
        self.grouping = grouping_was
        return ir.Var(
            '{0}__{1}'.format(convert_symbol(tree[0]), rhs),
            None
        )

    def walk_binop_numeric(self, tree):
        assert len(tree) == 2
        assert len(tree[1]) == 2
        grouping_was = self.grouping
        self.grouping = False
        retval = ir.Var(
            '{0}__{1}__{2}'.format(
                self.walk_expression(tree[1][0]),
                convert_symbol(tree[0]),
                self.walk_expression(tree[1][1]),
            ), None
        )
        self.grouping = grouping_was
        if tree[0] not in ast.binary_arithmetic_operators:
            self.comparisons.add(retval)
        return retval

    def walk_case(self, tree):
        assert len(tree) == 2
        cases = [
            '{} : {};'.format(
                self.walk_expression(pair[0]),
                self.walk_expression(pair[1]),
            )
            for pair in tree[1]
        ]
        return 'case {} esac'.format(
            ' '.join(cases)
        )

    def walk_cardinality_expressions(self, tree):
        ## TODO: test and debug
        assert len(tree[1]) > 0
        constraint = {
            ir.ONE_OR_MORE: '> 0',
            ir.ONE_AT_MOST: '<= 1',
            ir.ONE_AND_ONLY_ONE: '= 1',
        }[tree[0]]
        return '(count({}) {})'.format(
            ', '.join([str(self.walk_expression(x)) for x in tree[1]]),
            constraint,
        )

    def walk_function_call(self, tree):
        return '{}({})'.format(
            self.walk_expression(tree[0]),
            ', '.join(
                [str(self.walk_expression(x)) for x in tree[1:]]
            )
        )


def convert_symbol(symbol):
    """Convert a symbol from AST/IR syntax to SMV syntax."""
    mapping = {
        ast.AND: '&',
        ast.OR: '|',
        ast.XOR: 'xor',
        ast.NOT: '!',
        ast.LT: 'lt',
        ast.LEQ: 'le',
        ast.GT: 'gt',
        ast.GEQ: 'ge',
        ast.MLT: 'mul',
        ast.SUB: 'min',
        ast.ADD: 'pls',
        ast.DIV: 'div',
        ast.NEG: 'neg',
        'ABS': 'ABS',
        'POS': 'pos',
        ir.EQ_BOOLEAN: '=',
        ir.NEQ_BOOLEAN: '!=',
        ir.EQ_NUMERIC: 'eq',
        ir.NEQ_NUMERIC: 'ne',
        ast.EQ: 'eq',
        ast.NEQ: 'ne',
        ast.BOOLEAN: 'boolean',
        ir.VAR: 'VAR',
        ir.IVAR: 'IVAR',
        ir.INIT: 'init',
        ir.NEXT: 'next',
    }
    for key in mapping:
        if key == symbol:
            return mapping[key]
    raise ir.ConversionError('Unrecognized symbol: {0}'.format(symbol))


def combine(infiles, metadatas, variables, loaded_plugins, plugin_options):
    """Combine multiple SMV components to form a single model.

    The input files `infiles` can be a mix of either JSON files
    containing IR or raw SMV files, and the metadata files `metadata`
    should be JSON files with additional metadata, such as
    abstractions (which are applied when combining the files).

    """
    _COMPARISONS.clear()
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

    if len(_COMPARISONS) > 0:
        output.append('-- Numeric comparisons, as Boolean variables:')
        for comparison in sorted(_COMPARISONS):
            output.extend(
                [
                    'IVAR ivar_{} : boolean;'.format(comparison),
                    'VAR {} : boolean;'.format(comparison),
                    'TRANS next({0}) = ivar_{0};'.format(comparison),
                ]
            )


    ## Make this an SMV module.
    initializing = ir.Var('initializing', None)
    header_ir = [
        ['MODULE', 'main'],
        [ast.ASSIGN, [[ir.INIT, initializing], ir.Var('TRUE', None)]],
        [ast.ASSIGN, [[ir.NEXT, initializing], ir.Var('FALSE', None)]],
    ]
    header = ir_to_lines(header_ir)
    for line in header + modules + output + raw:
        print(line.strip())


def ir_to_lines(tree):
    """Convert the IR `tree` to lines of SMV code."""
    ir_walker = IRWalker(tree)
    ir_walker.walk()
    _COMPARISONS.update(ir_walker.comparisons)
    return ir_walker.lines


def postprocess(loaded_plugins):
    """Post-process the test results in the current directory."""
    results = {}
    times = {}

    ## Find the output files.
    files = os.listdir('.')
    cex_suffix = '.cex'
    prop_suffix = '.prop'
    cex_paths = []
    prop_paths = []
    for fname in files:
        if fname.endswith(cex_suffix):
            cex_paths.append(fname)
        elif fname.endswith(prop_suffix):
            prop_paths.append(fname)
    ## TODO: make sure that `cex` and `prop` match up
    cex_paths = sorted(cex_paths)
    prop_paths = sorted(prop_paths)

    ## Read the output.
    cexs = [_parse_counterexamples(x) for x in cex_paths]
    props = [_parse_properties(x) for x in prop_paths]
    timing_infos = [_parse_timing_info(x) for x in cex_paths]

    ## Apply any plugins that handle specific result types.
    active_plugins = plugins.actions.get_active_plugins(
        loaded_plugins, plugins.actions.POSTPROCESS
    )
    for idx, cex in enumerate(cexs):
        prop = props[idx]
        for plugin in active_plugins:
            categories = plugin.get_postprocessing_categories()
            plugin_results = _postprocess_worker(cex, prop, categories)
            _merge_dicts_of_sets(results, plugin_results)

    ## Get the timing information.
    for idx, cex_path in enumerate(cex_paths):
        timing_info = timing_infos[idx]
        name = cex_path[:-len(cex_suffix)]
        times[name] = timing_info
    with open('timing.json', 'w') as f:
        json.dump(
            times, f,
            indent=2, separators=(',', ': '), sort_keys=True
        )
        f.write('\n')

    ## Print the results.
    if False:
        for key in sorted(results):
            value = results[key]
            print('## {} ({})'.format(key, len(value)))
            for label in sorted(value):
                print(label)
    with open('summary.json', 'w') as f:
        results_serializable = {
            key: sorted(results[key])
            for key in sorted(results)
        }
        json.dump(
            results_serializable, f,
            indent=2, separators=(',', ': '), sort_keys=True
        )
        f.write('\n')


def _postprocess_worker(cex, prop, categories):
    results = {}
    for p in prop:
        property_specification = p[0][2].strip()
        property_logic = p[1][0]
        name = p[1][3]
        ## Find the matching result.
        for c in cex:
            counterexample_specification = c[1].strip()
            counterexample_logic = c[0]
            if counterexample_specification == property_specification:
                if property_logic == 'CTL':
                    if counterexample_logic[0] == 'specification':
                        break
                if property_logic == 'SYNTH':
                    if counterexample_logic[0] == '(SYNTH)':
                        break
        else:
            assert False
        outcome = c[-1]

        for category in categories:
            result_type = category[0]
            property_type = category[1]
            outcome_test = category[2]
            if result_type not in results:
                results[result_type] = set()
            if name.startswith(property_type):
                if outcome == outcome_test:
                    label = name[len(property_type)+1:]
                    results[result_type].add(label)

    return results


def _merge_dicts_of_sets(current, new):
    """Merge the elements of `new` into `current` (via set union).

    Both `new` and `current` must be `dict`s whose values are `set`s.
    This modifies `current`.

    """
    for key in new:
        if key in current:
            current[key] |= new[key]
        else:
            current[key] = new[key]


def _parse_counterexamples(path):
    """Parse the counterexample file `path`."""
    BEGIN = pyparsing.Literal('--')
    LPAR = pyparsing.Literal('(')
    RPAR = pyparsing.Literal(')')
    TYPE = pyparsing.Combine(LPAR + pyparsing.Word(pyparsing.alphas) + RPAR)
    SPECIFICATION = pyparsing.Literal('specification')
    IS = pyparsing.Literal('is')
    OUTCOME = (pyparsing.Literal('true') | pyparsing.Literal('false'))

    result = pyparsing.Group(
        BEGIN.suppress()
        + pyparsing.Group(pyparsing.Optional(TYPE) + SPECIFICATION)
        + pyparsing.SkipTo(IS + OUTCOME, include=True)
    )

    with open(path) as f:
        lines = f.readlines()
    matches = []
    for line in lines:
        if not line.startswith('--'):
            continue
        else:
            try:
                match = result.parseString(line)[0].asList()
            except pyparsing.ParseException:
                continue
            matches.append(match)
    return matches


def _parse_properties(path):
    """Parse the properties file `path`."""
    ## First line.
    NUMBER = pyparsing.Word(pyparsing.nums)
    COLON = pyparsing.Literal(':')
    line_1 = pyparsing.Group(NUMBER + COLON + pyparsing.restOfLine)
    ## Second line.
    LSQ = pyparsing.Literal('[')
    RSQ = pyparsing.Literal(']')
    STUFF = pyparsing.Regex(r'[\w/]+')
    line_2 = pyparsing.Group(
        LSQ.suppress() + STUFF + STUFF + STUFF + STUFF + RSQ.suppress()
    )
    ## Parse line-by-line.
    first_lines = []
    second_lines = []
    with open(path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(('***', '---')) or len(stripped) == 0:
            continue
        try:
            parsed = line_1.parseString(line)
            first_lines.append(parsed.asList()[0])
            continue
        except pyparsing.ParseException:
            pass
        try:
            parsed = line_2.parseString(line)
            second_lines.append(parsed.asList()[0])
            continue
        except pyparsing.ParseException:
            pass
    assert len(first_lines) == len(second_lines)
    ##
    return list(zip(first_lines, second_lines))


def _parse_timing_info(path):
    """Read the timing information form the SMV output at `path`."""
    ## Define a parser for the timing info line.
    DIGITS = pyparsing.Word(pyparsing.nums)
    NUMBER = pyparsing.Combine(DIGITS + '.' + DIGITS)
    BEGINNING = 'User time'
    parser = BEGINNING + NUMBER + pyparsing.Word(pyparsing.alphas)
    ## Find the lines in the file with timing info.
    with open(path) as f:
        lines = f.readlines()
    relevant_lines = [line for line in lines if line.startswith(BEGINNING)]
    if not len(relevant_lines) == 1:
        logger.warning(path)
        assert False
    relevant_line = relevant_lines[0]
    ## Parse the timing info line.
    parsed = parser.parseString(relevant_line).asList()
    user_time = float(parsed[1])
    units = parsed[2]
    return (user_time, units)
