## Copyright (c) 2016-2018, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import argparse
import cProfile
import importlib

from . import ast
from . import ir
from . import scheduling
from . import smt
from . import smv
from . import st
from . import utils

logger = utils.logging.getLogger(__name__)


def load_plugin(loaded_plugins, plugin_name):
    """Load the plugin `plugin_name`.  This modifies `loaded_plugins` in
    place.

    """
    try:
        plugin = importlib.import_module(
            '.plugins.{0}.{0}'.format(plugin_name), package=__package__
        )
        if plugin not in loaded_plugins:
            loaded_plugins.append(plugin)
            logger.debug(
                'Loaded the "{}" plugin.'.format(plugin.NAME)
            )
        else:
            logger.warning(
                'Tried to load the "{}" plugin multiple times, skipping.'
                .format(plugin.NAME)
            )
    except ImportError as e:
        logger.error(
            'Failed to load the "{}" plugin: {}.'.format(plugin_name, e)
        )


def run(profiler):
    ## Define the command-line arguments.
    argument_parser = argparse.ArgumentParser(
        description=(
            'Convert Structured Text (ST) code to an SMV model.'
        )
    )
    ## Top-level commands (one and only one).
    commands = argument_parser.add_mutually_exclusive_group(required=True)
    commands.add_argument(
        '--convert',
        action='store_true', default=False,
        help='convert an ST input file to an SMV model'
    )
    commands.add_argument(
        '--combine',
        action='store_true', default=False,
        help=(
            'combine one or more files '
            '(either raw SMV files, '
            'or JSON files containing an intermediate representation) '
            'into a single SMV model'
        )
    )
    commands.add_argument(
        '--parse',
        action='store_true', default=False,
        help='parse the ST input and print the abstract syntax tree (AST)'
    )
    commands.add_argument(
        '--postprocess',
        action='store_true', default=False,
        help='postprocess the results in the current directory'
    )
    commands.add_argument(
        '--read-timing-data',
        action='store_true', default=False,
        help='read historical timing data'
    )
    commands.add_argument(
        '--check-schedule',
        action='store_true', default=False,
        help='check a schedule'
    )
    ## Other arguments.
    _default = 'smv'
    argument_parser.add_argument(
        '--format', '-f',
        type=str, action='store', default=_default,
        choices=('smt', 'smv'),
        help=('set the format to convert to (default: {})'.format(_default))
    )
    argument_parser.add_argument(
        '--input', '-i',
        nargs='+', type=str, action='store', default=[],
        help='specify one or more input files'
    )
    argument_parser.add_argument(
        '--output-directory',
        type=str, action='store', default=None,
        help='specify the directory in which to store the output'
    )
    _default = 'SynthSMV'
    argument_parser.add_argument(
        '--solver-path',
        type=str, action='store', default=_default,
        help=(
            'specify the path to the solver executable (default: {})'
            .format(_default)
        )
    )
    argument_parser.add_argument(
        '--solver-arguments',
        type=str, action='store', default='',
        help=(
            'provide a list of arguments to pass when calling the solver; '
            'this should be used as --solver-arguments=\'arg1 arg2 etc\' '
            '(note the equals sign and the quotes) '
            'due to a bug/limitation in Python\'s "argparse" module: '
            'https://bugs.python.org/issue9334'
        )
    )
    argument_parser.add_argument(
        '--plugins',
        nargs='+', type=str, action='store', default=[],
        help='specify a list of plugins to (attempt to) load'
    )
    argument_parser.add_argument(
        '--plugin-options',
        nargs='+', type=str, action='store', default=[],
        help=(
            'specify some plugin-specific options '
            'as a list, separated by spaces; '
            'each option should have the form "name" or "name=value" '
            '(without the quotes)'
        )
    )
    argument_parser.add_argument(
        '--metadata', '-m',
        nargs='+', type=str, action='store', default=[],
        help='specify separate metadata files (JSON)'
    )
    argument_parser.add_argument(
        '--variables',
        nargs='+', type=str, action='store', default=None,
        help='declare a list of variables that appear in the specification'
    )
    argument_parser.add_argument(
        '--key-scheduling-unit',
        type=str, action='store', default=None,
        help='specify the "key" unit for scheduling'
    )
    _default = 'info'
    argument_parser.add_argument(
        '--verbosity', '-v',
        type=str, action='store', default=_default,
        choices=('error', 'warn', 'info', 'debug'),
        help=(
            'set the verbosity level; debug is the highest (default: {})'
            .format(_default)
        )
    )
    argument_parser.add_argument(
        '--profile',
        action='store_true', default=False,
        help='print profiling/performance information for `st2smv` itself'
    )
    argument_parser.add_argument(
        '--debug-args',
        nargs = '+', type=str, action='store', default=None,
        help='specify extra arguments for debugging (unstable!)'
    )

    ## Parse (and check) the command-line arguments.
    args = argument_parser.parse_args()
    if args.convert and args.output_directory is None:
        argument_parser.error(
            'the `--convert` command reauires that '
            '`--output-directory` is specified'
        )
    if (args.convert or args.parse) and len(args.input) != 1:
        argument_parser.error(
            'the `--convert` and `--parse` commands '
            'require exactly one (1) `--input` (got {})'
            .format(len(args.input))
        )

    ## Start the profiler, if necessary.
    if args.profile:
        profiler.enable()

    verbosity_map = {
        'error': utils.logging.ERROR,
        'warn': utils.logging.WARN,
        'info': utils.logging.INFO,
        'debug': utils.logging.DEBUG,
    }
    utils.logging.basicConfig(level=verbosity_map[args.verbosity])

    ## Set up the plugins.
    loaded_plugins = []
    for plugin_name in args.plugins:
        load_plugin(loaded_plugins, plugin_name)

    ## Set up the plugin options.
    plugin_options = {}
    for string in args.plugin_options:
        pieces = string.split('=')
        ## Make sure one of the loaded plugins handles this option.
        option = pieces[0]
        option_is_handled = False
        for loaded_plugin in loaded_plugins:
            if option in loaded_plugin.OPTIONS:
                option_is_handled = True
                (option_type, option_help) = loaded_plugin.OPTIONS[option]
            if option_is_handled:
                break
        if not option_is_handled:
            raise LookupError(
                'Unrecognized plugin option: {}'.format(string)
            )
        ## Store the option value.
        if len(pieces) == 1:
            assert option_type is bool
            plugin_options[option] = True
        else:
            assert len(pieces) == 2
            plugin_options[option] = option_type(pieces[1])

    ## Run the command.
    if args.convert:
        _ = ir.st_to_ir(
            args.input[0],
            metadata_paths=args.metadata,
            directory=args.output_directory,
            loaded_plugins=loaded_plugins,
            plugin_options=plugin_options,
        )
    if args.parse:
        ast.dump_ast(args.input[0], st, loaded_plugins)
    if args.combine:
        if args.format == 'smv':
            combiner = smv.combine
        else:
            assert args.format == 'smt'
            combiner = smt.combine
        combiner(
            args.input, args.metadata, args.variables,
            loaded_plugins, plugin_options,
        )
    if args.postprocess:
        assert args.format == 'smv'
        smv.postprocess(loaded_plugins)
    if args.read_timing_data:
        scheduling.read_timing_data(
            args.input[0], directory=args.output_directory
        )
    if args.check_schedule:
        scheduling.check_schedule(args=args)


def main():
    profiler = cProfile.Profile()
    try:
        run(profiler)
    except KeyboardInterrupt as e:
        raise e
    finally:
        profiler.disable()
        if len(profiler.getstats()) > 0:
            profiler.dump_stats('st2smv.prof')


if __name__ == '__main__':
    main()
