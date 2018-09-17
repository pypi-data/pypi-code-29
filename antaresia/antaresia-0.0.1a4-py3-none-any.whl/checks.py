import os
import shutil
import sys

import mypy.api

__all__ = ["check_mypy"]


def check_mypy(filename: os.PathLike):
    # TODO add pyi file to config_functions to check those ones
    stdout, stderr, exit_code = mypy.api.run(["--follow-imports=skip", os.fsdecode(filename)])
    if exit_code != 0:
        print(stdout, file=sys.stderr)
        if stderr:
            print(stderr, file=sys.stderr)
        exit(exit_code)
