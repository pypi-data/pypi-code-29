from __future__ import unicode_literals
from importlib import import_module
from . import builtins_module, text


def find_innermost_module(full_qualifier):
    """
    This function find the innermost module or package specified inside module_path, it does this by trying importing
    full_qualifier and the stripping the last name from it and trying again. If the qualifier is a builtin then it
    returns two empty strings.

    >>> find_innermost_module("logging.config.fileConfig")
    ('logging.config', 'fileConfig')

    >>> find_innermost_module("logging.config")
    ('logging.config', '')

    >>> find_innermost_module("logging")
    ('logging', '')

    >>> find_innermost_module("filter")
    ('', '')

    :type full_qualifier: str
    :param full_qualifier: A string representing a package, a module or an attribute inside one of them.
    :return: A tuple where the first element is the module or package name and the second element is an empty string or
    an the attribute name. If full_qualifier is a builtin then both values are empty
    """

    module_package = ""
    attribute = ""

    for i in range(full_qualifier.count(".") + 1):
        try:
            module_package = full_qualifier.rsplit('.', i)[0]
            _ = import_module(module_package)
            attribute = ".".join(full_qualifier.rsplit('.', i)[1:])
            break
        except ImportError:
            module_package = ""
            attribute = ""

    if module_package != "":
        # When full_qualifier is a builtin then we don't have any value set.
        assert module_package + ("." + attribute if attribute != "" else "") == full_qualifier

    return text(module_package), text(attribute)


def extract_builtin_attribute(attribute_name):
    """
    Return the attribute with name 'attribute_name' from the builtins' definitions, raise an exception if it doesn't
    exists

    :param attribute_name:
    :return:
    """
    return getattr(builtins_module, attribute_name)
