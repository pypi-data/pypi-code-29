from typing import Any, Dict
import ast
import copy
import os
import types

TYPES_BLACKLIST = [types.FunctionType]  # TODO other things like classes
AST_IMPORT = [ast.Import, ast.ImportFrom]
AST_LOOP = [ast.For, ast.While]


def exclude_value(key: str, value):
    if key.startswith("__"):  # TODO consider if this is really needed
        return True
    if type(value) in TYPES_BLACKLIST:
        return True
    return False


def filter_values(dictionary: Dict[str, Any]) -> dict:
    return {
        key: value for key, value in dictionary.items() if not exclude_value(key, value)
    }


# TODO optionally allow loops


def excluded_node(node: ast.AST, filename: os.PathLike):
    """
    Excludes invalid node types.
    Imports are ignored to allow using IDEs and type checkers against configuration files
    Configurations with For and While Loops are rejected.
    """
    node_type = type(node)
    if node_type in AST_IMPORT:
        return True
    if node_type in AST_LOOP:
        raise Exception(
            f"Invalid Configuration in {filename} ({node.lineno}:{node.col_offset})"
        )
    return False


def filter_ast(node: ast.Module, filename: os.PathLike):
    node = copy.deepcopy(node)
    node.body = [
        sub_node for sub_node in node.body if not excluded_node(sub_node, filename)
    ]
    return node
