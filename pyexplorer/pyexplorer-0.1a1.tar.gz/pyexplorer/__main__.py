from __future__ import unicode_literals
from .interactive import interactive
from .filters import dir_filter
from .utilities import find_innermost_module, extract_builtin_attribute
from .discovery import discovery_package, discovery_module, discovery_attribute
from .formatters import module_format, attribute_format
from argparse import ArgumentParser
from importlib import import_module
import logging
import types

logger = logging.getLogger(__name__)


def parse_args():
    """
    Parse command line arguments
    :return: an object of command line arguments
    """
    parser = ArgumentParser()
    # noinspection PyTypeChecker
    parser.add_argument("module", type=str, nargs="?", help="Module or package name.")
    parser.add_argument("-a", action="store_true", help="Show everything inside the module/package.")
    # noinspection PyTypeChecker
    parser.add_argument("--level", type=int, default=0, help="List all methods inherited up to this level.")

    return parser.parse_args()


def main():
    args = parse_args()

    if args.module is None:
        logger.debug("module is None, starting interactive session.")
        interactive()
        return

    # list of filtering functions
    filters = []
    if not args.a:
        filters.append(dir_filter)

    # <package>.<module>.<attribute>.<attribute> -> "<package>.<module>", "<attribute>.<attribute>"
    module_package_name, attribute_name = find_innermost_module(args.module)

    if not module_package_name and not attribute_name:
        # builtin
        # if module_package_name is empty we are processing a builtin attribute
        attribute = extract_builtin_attribute(args.module)

        c = discovery_attribute(attribute, lambda x: all([f(x) for f in filters]))
    elif module_package_name and not attribute_name:
        # module or package
        # everything for python is a module, at least is imported in the same way
        module_package = import_module(module_package_name)

        # it the module has the __path__ attribute then is a package
        if hasattr(module_package, "__path__"):
            c = discovery_package(module_package, lambda x: all([f(x) for f in filters]))
        else:
            c = discovery_module(module_package, lambda x: all([f(x) for f in filters]))
    else:
        # attribute inside module or package
        module_package = import_module(module_package_name)

        parent_scope = module_package
        for i in range(attribute_name.count(".") + 1):
            attribute_name = attribute_name.split(".")[i]
            attribute = getattr(parent_scope, attribute_name)
            parent_scope = attribute

        c = discovery_attribute(attribute, lambda x: all([f(x) for f in filters]))

    for content in c:
        if isinstance(content, types.ModuleType):
            module_format(content)
        else:
            attribute_format(content)


if __name__ == "__main__":
    main()
