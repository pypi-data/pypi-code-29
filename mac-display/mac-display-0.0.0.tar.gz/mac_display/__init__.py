#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd

@public
def sleep():
    cmd = ["pmset","displaysleepnow"]
    runcmd.run(cmd)

@public
def wake():
    cmd = ["caffeinate","-u","-t","1"]
    runcmd.run(cmd)
