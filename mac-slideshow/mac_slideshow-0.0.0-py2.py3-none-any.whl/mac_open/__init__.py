#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd


def _run(args):
    runcmd.run(["open"] + args)._raise()


@public
def app(*names):
    _run(["-a"] + list(names))


@public
def path(*paths):
    _run(["-R"] + list(paths))


@public
def url(*urls):
    _run(list(urls))
