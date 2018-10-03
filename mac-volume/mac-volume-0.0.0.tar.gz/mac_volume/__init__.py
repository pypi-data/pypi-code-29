#!/usr/bin/env python
# -*- coding: utf-8 -*-
import applescript
from public import public


def _execute(code):
    return applescript.run(code).out


@public
def get():
    out = _execute("output volume of (get volume settings)")
    return int(out)


@public
def set(volume):
    _execute("set volume output volume %s" % volume)


@public
def mute():
    _execute("set volume with output muted")


@public
def muted():
    return "true" in _execute("output muted of (get volume settings)")


@public
def unmute():
    _execute("set volume without output muted")
