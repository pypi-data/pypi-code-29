#!/usr/bin/env python
import subprocess
from public import public


@public
def kill(pid):
    try:
        args = ["kill"]+list(map(str,pid))
    except TypeError:
        args = ["kill"]+list(map(str,[pid]))
    process = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = process.communicate()
    return err.decode()
