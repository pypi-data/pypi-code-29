#!/usr/bin/env python
import find as _find
from public import public
import runcmd

@public
def find(search):
    path = "/Library/Desktop Pictures"
    files = _find.files(path)
    matches = []
    for f in files:
        if "/." not in f and search in f.replace(path,""):
            matches.append(f)
    return matches

@public
def get():
    return runcmd.run(["wallpaper"])._raise().out


@public
def set(path):
    return runcmd.run(["wallpaper", path])._raise()
