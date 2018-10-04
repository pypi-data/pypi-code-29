import ast
import os
import shutil
import sys

import mypy.api

from .exceptions import MyPyFail

__all__ = ["check_mypy"]


# TODO pass filename here
def check_ast_nodes(node: ast.Module, filename: str = "."):
    """
    Checks if ast doesn't have disalowed constructs
    """
    for sub_node in ast.walk(node):
        if isinstance(sub_node, ast.Attribute):
            attribute = sub_node.attr
            if attribute.startswith("__"):
                # TODO Test
                raise Exception(
                    f"{filename}:{sub_node.lineno}: error: "
                    f"Accessing private attribute {attribute} is forbidden."
                )


def check_mypy(filename: os.PathLike):
    # TODO add pyi file to config_functions to check those ones
    stdout, stderr, exit_code = mypy.api.run(
        ["--follow-imports=skip", os.fsdecode(filename)]
    )
    if exit_code != 0:
        print(stdout, file=sys.stderr)
        if stderr:
            print(stderr, file=sys.stderr)
        raise MyPyFail()
