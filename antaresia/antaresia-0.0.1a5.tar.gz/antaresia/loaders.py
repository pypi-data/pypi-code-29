from typing import Optional
import ast
import os
import functools
import typing

from .checks import check_ast_nodes, check_mypy
from .filters import filter_values, filter_ast

EXPRESSION_SEPARATOR = "### antaresia return:"


def load_string(code: str, filename: os.PathLike = ".", variables: Optional[dict]=None) -> dict:
    if filename != ".":  # if we have a real filename
        check_mypy(filename)
    # config_functions needs to be imported here because it needs ``load`` to be defined
    from .config_functions import include_config, read

    expression: Optional[str]
    if EXPRESSION_SEPARATOR in code:
        code, expression = code.split(EXPRESSION_SEPARATOR)
    else:
        expression = None

    root_node: ast.Module = ast.parse(code)
    check_ast_nodes(root_node)
    filtered_node = filter_ast(root_node, filename)
    # Globals will be available in the configuration
    config_globals = {"include_config": include_config, "read": read}
    pre_provided = set(config_globals.keys())
    # TODO do this only in python 3.6 (annotations are not evaluated by default on 3.7)
    for var in typing.__all__:
        config_globals[var] = getattr(typing, var)
    if variables:  # add user provided variables
        config_globals.update(variables)
        pre_provided.update(variables.keys())

    compiled_code = compile(filtered_node, filename, "exec")
    exec(compiled_code, config_globals)
    values = filter_values(config_globals, pre_provided=pre_provided)
    if expression is not None:
        configuration = eval(expression, {}, values)
    else:
        configuration = values
    return configuration


def load(filename: os.PathLike, variables: Optional[dict]=None) -> dict:
    with open(filename) as configuration_file:
        configuration_source = configuration_file.read()
        return load_string(configuration_source, filename, variables)
