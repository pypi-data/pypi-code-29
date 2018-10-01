#!/usr/bin/env python
import subprocess
from public import public


def _kill_args(pid):
    try:
        return ["kill"] + list(map(str, pid))
    except TypeError:
        return ["kill"] + list(map(str, [pid]))


@public
def kill(pid):
    if not pid:
        return
    args = _kill_args(pid)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return err.decode().rstrip()
