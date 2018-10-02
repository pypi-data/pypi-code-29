#!/usr/bin/env python
from public import public
import runcmd

"""
Classic

"""


DOMAIN = "com.apple.ScreenSaver.iLifeSlideShows"
KEY = "styleKey"


@public
def read():
    cmd = ["defaults", "-currentHost", "read", DOMAIN, KEY]
    return runcmd.run(cmd).out


@public
def write(path):
    old = read()
    if path != old:
        cmd = ["defaults", "-currentHost", "write", DOMAIN, KEY, path]
        runcmd.run(cmd)._raise()
        runcmd.run(["killall", "cfprefsd", "System Preferences"])
