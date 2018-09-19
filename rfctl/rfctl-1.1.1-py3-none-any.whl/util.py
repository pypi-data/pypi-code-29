# -*- coding: utf-8 -*-

import subprocess
import sys


def gen_sh_util(cwd: str, pipe=False):
    if pipe:
        def sh(*cmds):
            return subprocess.run(
                cmds,
                cwd=cwd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
    else:
        def sh(*cmds):
            return subprocess.run(
                cmds,
                cwd=cwd,
                shell=True,
                stdout=sys.stdout,
                stderr=sys.stderr,
                universal_newlines=True,
            )
    return sh
