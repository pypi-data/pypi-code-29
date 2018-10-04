from subprocess import call

from typing import List

import os


def run(cmd_args: List[str], silent=True):
    """
    Runs a command with its arguments.
    """

    if silent:
        with open(os.devnull, 'w') as fnull:
            status = call(cmd_args, stdout=fnull)
    else:
        status = call(cmd_args)

    if status != 0:
        # TODO: Retrieve cmd stdout/stderr
        raise OSError(f"an error ({status})  occured while running command {cmd_args[0]}")
