#!/usr/bin/env python3
import subprocess
import sys


# Wrap the Hugo command.
cmd = []
cmd.append('hugo')
if sys.argv[1:]:
    cmd.append(sys.argv[1:])
subprocess.call(cmd)
