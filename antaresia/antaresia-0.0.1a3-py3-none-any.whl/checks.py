import os
import shutil
import tempfile

import mypy.api

__all__ = ['check_mypy']

def check_mypy(filename: os.PathLike):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, 'config.py')
        shutil.copyfile(filename, temp_file)
        # TODO add pyi file to config_functions to check those ones
        stdout, stderr, exit_code = mypy.api.run(['--follow-imports=skip', temp_file])
        if exit_code != 0:
            print(stdout.replace(temp_file, filename))
            if stderr:
                print(stderr)
            exit(exit_code)