# /usr/bin/env python
# coding=utf-8

import sys
import subprocess


def run_cmd(args, shell=False, wait=True, print_command=True):
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=shell)
    if print_command:
        print " ".join(args)

    if wait:
        stdout, stderr = p.communicate()
        if stderr:
            raise Exception("error occurs while running cmd, error is: %s", stderr)
        return stdout
