#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd


def run(args, background=False):
    r = runcmd.run(["say"] + args, background=background)
    if not background:
        r._raise()


@public
def string(value, background=False):
    run([str(value)], background=background)


@public
def file(path, background=False):
    string = open(path).read()
    run([str(string)], background=background)
