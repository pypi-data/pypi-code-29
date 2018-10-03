#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd

"""
cli detect sleeping:
echo $(ioreg -n IODisplayWrangler | grep -i IOPowerManagement | perl -pe 's/^.*DevicePowerState\"=([0-9]+).*$/\1/')/4 | bc
"""


@public
def sleep():
    cmd = ["pmset", "displaysleepnow"]
    runcmd.run(cmd)


@public
def sleeping():
    out = runcmd.run(["ioreg", "-n", "IODisplayWrangler"])._raise().out
    state = int(out.split('"DevicePowerState"=')[1][0])  # 0-4
    return state in [0, 1]


@public
def wake():
    cmd = ["caffeinate", "-u", "-t", "1"]
    runcmd.run(cmd)
