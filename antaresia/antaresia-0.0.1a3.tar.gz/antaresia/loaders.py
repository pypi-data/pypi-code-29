from typing import Optional
import ast
import os
import functools
import typing

from .checks import check_mypy
from .filters import filter_values, filter_ast

EXPRESSION_SEPARATOR = '### antaresia return:'

def load_string(code: str, filename: str= '.') -> dict:

    if filename != '.':  # if we have a real filename
        check_mypy(filename)
    # config_functions needs to be imported here because it needs ``load`` to be defined
    from .config_functions import include_config, read

    if EXPRESSION_SEPARATOR in code:
        code, expression = code.split(EXPRESSION_SEPARATOR)
    else:
        expression = None

    root_node: ast.Module = ast.parse(code)
    filtered_node = filter_ast(root_node, filename)
    globals = {'include_config': include_config,
               'read': read}
    # TODO do this only in python 3.6
    for var in typing.__all__:
        globals[var] = getattr(typing, var)
    locals = {}
    code = compile(filtered_node, filename, 'exec')
    exec(code, globals, locals)
    values = filter_values(locals)
    if expression is not None:
        configuration = eval(expression, {}, values)
    else:
        configuration = values
    return configuration

def load(filename: os.PathLike) -> dict:
    with open(filename) as configuration_file:
        configuration_source = configuration_file.read()
        return load_string(configuration_source, filename)