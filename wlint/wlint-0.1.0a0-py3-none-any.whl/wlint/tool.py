#!/usr/bin/python3

"""Functionality to help write and use wlint tools"""

import argparse
import errno
import sys

import wlint.plugin
import wlint.purify

_INPUT_PURIFIERS = wlint.plugin.query_plugins('wlint.puririfiers')


def _print_input_types():
    for input_type in sorted(_INPUT_PURIFIERS):
        print("{} - {}".format(input_type, _INPUT_PURIFIERS[input_type][1]))


class Tool:

    """
    A wlint tool.

    This class isn't expected to be used directly, but instead be subclassed.
    """

    def __init__(self, *args, **kwargs):
        self._parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            *args, **kwargs)

        # add common arguments
        self._parser.add_argument("files",
                                  help="Files to process.", nargs="*",
                                  metavar="file")
        self.add_argument(
            "--input-type",
            help="Type of input file.",
            default="text")
        self.add_argument(
            "--list-input-types",
            action='store_true',
            help="List supported input types.",
            default=argparse.SUPPRESS)

        self.sort_methods = None

    def add_argument(self, *args, **kwargs):
        """
        Add a command-line argument.

        Any arguments will be passed to the underlying command-line parser
        object.
        """
        self._parser.add_argument(*args, **kwargs)

    def add_sort(self, sort_methods):
        """
        Support sort options via command-line arguments.

        This just adds the relevant command-line options; it's the
        responsibility of each Tool to perform its own sorting.

        Arguments:
        sort_methods -- A list of tuples representing valid sorts for the tool.
                        Each item in the list should contain 1) a name (this
                        will be valid options for the user to select) and 2) a
                        short description of the sort.  The first item in the
                        list wll be the defualt sort.
        """
        self.add_argument(
            "--sort",
            help="Method to sort output.  Options are: {}".format(
                ", ".join([i[0] for i in sort_methods])),
            default=sort_methods[0][0])
        self.add_argument(
            "--list-sorts",
            action='store_true',
            help="List supported sort methods.",
            default=argparse.SUPPRESS)
        self.sort_methods = sort_methods

    def execute(self, parsed_args):
        """
        Execute the tool with parsed_args.

        This is expected to be overriden by subclasses.  The default
        implementation does nothing.

        Arguments:
        parsed_args -- Parsed command-line arguments.

        Return:
        Either a list of missing files or something that evaluates to False.
        If a tool needs to generate missing files, the best option is to use
        the iterate_files function (its return value is a missing files list).
        """
        pass


def get_purifier(parsed_args):
    """
    Return a purifier function based on the command-line arguments.

    Arguments:
    parsed_args -- a set of parsed command-line arguments

    Return:
    A purification function.
    """
    purifier = _INPUT_PURIFIERS.get(parsed_args.input_type)[0]
    if not purifier:
        raise ValueError(
            "'{}' is not a supported input type".format(parsed_args.input_type))
    return purifier


def iterate_files(parsed_args, process_fn):
    """
    Iterate over all files listed in the command line and execute a function.

    Arguments:
    parsed_args -- a parsed set of command-line arguments
    process_fn -- A function to execute for each file.  It will be passed the
                  file handle as the only argument.

    Return:
    A list of missing files (i.e., they were specified but couldn't be opened).
    """
    if parsed_args.files:
        missing_files = []
        for filename in parsed_args.files:
            try:
                with open(filename, 'r') as read_file:
                    process_fn(read_file)
            except FileNotFoundError:
                missing_files.append(filename)
        return sorted(missing_files)
    # no files provided, so default to stdin
    process_fn(sys.stdin)
    return []


def _check_special_options(tool, parsed_args):
    def _list_sorts():
        for (name, description) in tool.sort_methods:
            print("{} - {}".format(name, description))

    def _list_input_types():
        for name, info in _INPUT_PURIFIERS.items():
            print("{} - {}".format(name, info[1]))

    if "list_sorts" in parsed_args and parsed_args.list_sorts:
        return _list_sorts
    elif "list_input_types" in parsed_args and parsed_args.list_input_types:
        return _list_input_types
    return None


def _parse_args(tool, *args, **kwargs):
    # pylint: disable=protected-access
    parsed_args = tool._parser.parse_args(*args, **kwargs)
    return parsed_args


def execute_tool(tool, args):
    """
    Execute a tool with given arguments.

    Execution involves the following:
      - parsing command-line arguments
      - checking for special arguments
      - calling the execute method on tool
      - printing a list of missing files if any exist

    Arguments:
    tool -- The tool to execute.  This must be an instance of Tool or a Tool
            subclass.
    args -- The command-line arguments to tool.
    """
    if args is None:
        args = sys.argv[1:]
    try:
        parsed_args = _parse_args(tool, args)
        special_fn = _check_special_options(tool, parsed_args)
        if special_fn:
            special_fn()
        else:
            missing_files = tool.execute(parsed_args)

            if missing_files:
                print(
                    "Error opening files: {}".format(
                        missing_files),
                    file=sys.stderr)
                exit(1)

    except IOError as error:
        if error.errno == errno.EPIPE:
            # This probably means we were piped into something that terminated
            # (e.g., head).  Might be a better way to handle this, but for now
            # silently swallowing the error isn't terrible.
            pass

    except Exception as error:  # pylint: disable=broad-except
        print("Error: {}".format(str(error)), file=sys.stderr)
        exit(1)
