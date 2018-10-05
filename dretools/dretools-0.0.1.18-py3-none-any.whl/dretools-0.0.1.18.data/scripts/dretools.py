#!python
"""

This file handles command line input to all DRETools. It determines whether to print the main help menu,
a function help menu (Note: All function help data is self-contained), or run a function.

The rest of DRETools can be found in the following directories:
examples/ - Contains files that can be used for example input.
features/ - Contains files for integration testing.
lib/      - Contains the sub-section classes.
lib/__init__.py - A dictionary mapping function names to their respective classes and functions.
test_data/     - Contains files for unit testing.

"""

import sys
import argparse
import os.path
from signal import signal, SIGPIPE, SIG_DFL

# from .lib import operations_dict

# from lib.main_script_helper_functions import get_main_help_string, import_from, __version__

# Fix import errors.
#from pathlib import Path # if you haven't already done so
#file = Path(__file__).resolve()
#print(file)
#print("==========================================")
#parent, root = file.parent, file.parents[1]
#print(parent, root)
#print("==========================================")
#sys.path.append(str(root))
#sys.path.append(str(parent))

from lib import operations_dict

# Additionally remove the current file's directory from sys.path
# try:
#    sys.path.remove(str(parent))
# except ValueError: # Already removed
#    pass


program_name = "dretools"


# Problem with broken pipe error (Errno-32) solved with
# http://newbebweb.blogspot.de/2012/02/python-head-ioerror-errno-32-broken.html
signal(SIGPIPE, SIG_DFL)
reserved_flags = (
    "--update-help",
    "--commands?",
    "--help", "-help", "-h", "--h",
)
help_menu_file = "dretools_docstring.txt"


def generate_help_str():
    """ Handles the main help output for DRETools

    1. The function first checks for a pre-built strings in /tmp as generating the string from scratch takes time.
    2. If pre-build string is not available it iterates over the dictionary in lib/__init__.py
    3. The first line of each doc string is read

    :return: joined_list - A string of possible operations formatted as a help string.
    """

    function_dicts = operations_dict
    offset = "    "
    out_list = []
    longest_name = 0

    # Get the longest name to calculate description offset.
    for main_type in function_dicts:
        for operation_name_el in function_dicts[main_type]:
            if len(operation_name_el) > longest_name:
                longest_name = len(operation_name_el)

    # Build the argparse help strings.
    for main_type in function_dicts:

        # Main types serve as headings for groups of operations.
        out_list.append(main_type)

        for operation_name_el in function_dicts[main_type]:

            # Generate the number of spaces we need to
            description_offset = "".join([" " for i in range(longest_name - len(operation_name_el))]) + " -"

            out_list.append("".join([
                offset,
                operation_name_el,
                description_offset,
                function_dicts[main_type][operation_name_el].__doc__.split("\n")[0]
            ]))

    joined_list = "\n".join(out_list)

    return joined_list


if len(sys.argv) > 1 and not sys.argv[1] in ("--help", "-help", "-h", "--h", "--commands?"):
    # Run an operation or function.

    # Get the base program name.
    program_name = os.path.basename(sys.argv[0])

    # The name of the operation should be the first argument.
    operation_name = sys.argv[1]

    # Rebase the sys.argv command, pretend the operation is the program that was ran.
    sys.argv = sys.argv[1:]

    # Helps catch cases where the argument supplied does not match the available operations.
    operation_found = False

    # Since we organize the data structure by headings, loop through each heading.
    for section_name in operations_dict:
        # Check for the operation name within each heading.
        if operation_name in operations_dict[section_name]:

            # Build the argument parser for the operation.
            parser = argparse.ArgumentParser(
                prog=" ".join((program_name, operation_name)),
                formatter_class=argparse.RawTextHelpFormatter,
                epilog="\n".join(operations_dict[section_name][operation_name].__doc__.split("\n")[1:])
            )

            # Run the operation.
            operations_dict[section_name][operation_name](parser)
            operation_found = True
            break

    if not operation_found:
        sys.stderr.write("function {} not found\n".format(operation_name))

else:
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    help_str = generate_help_str()
    parser.add_argument('operation', type=str, nargs=1, help='Operations Available:\n' + help_str)
    parser.print_help()
