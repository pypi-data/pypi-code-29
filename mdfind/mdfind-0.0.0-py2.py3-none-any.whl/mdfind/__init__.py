#!/usr/bin/env python
from public import public
import runcmd
import values


def _args(query=None, name=None, onlyin=None):
    args = []
    if name:
        args += ["-name", name]
    for path in values.get(onlyin):
        args += ["-onlyin", path]
    if query:
        args += [query]
    return list(args)

@public
def mdfind(args):
    cmd = ["mdfind"] + list(args)
    return runcmd.run(cmd)._raise().out


@public
def count(query=None, name=None, onlyin=None):
    args = ["-count"]+_args(query=query, name=name,onlyin=onlyin)
    return int(mdfind(args))


@public
def name(name, onlyin=None):
    args = _args(name=name, onlyin=onlyin)
    return mdfind(args).splitlines()


@public
def query(query, onlyin=None):
    args = _args(query=query, onlyin=onlyin)
    return mdfind(args).splitlines()

