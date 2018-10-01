#!/usr/bin/env python
import subprocess
from public import public


@public
def pgrep(pattern):
    args = ["pgrep",str(pattern)]
    process = subprocess.Popen(args,stdout=subprocess.PIPE)
    stdoutdata, stderrdata = process.communicate()
    return list(map(int,stdoutdata.decode().splitlines()))
