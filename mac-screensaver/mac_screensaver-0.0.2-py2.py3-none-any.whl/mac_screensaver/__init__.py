#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import pgrep
import runcmd


@public
def _run(args):
    cmd = ["screensaver"] + list(args)
    return runcmd.run(cmd)._raise().out


@public
def clock():
    return bool(_run(["clock"]))


@public
def idle():
    return bool(_run(["idle"]))


@public
def kill():
    _run(["kill"])


@public
def name():
    return _run(["name"])


@public
def names():
    return _run(["names"]).splitlines()


@public
def pid():
    pids = pgrep.pgrep("ScreenSaverEngine")
    if pids:
        return pids[0]


@public
def start():
    _run(["start"])


@public
def style():
    return _run(["style"])
