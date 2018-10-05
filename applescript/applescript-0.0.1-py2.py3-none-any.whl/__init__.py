#!/usr/bin/env python
import os
import only
from public import public
import runcmd
import temp
import applescript.tell


@only.osx
@public
def run(applescript, background=False):
    path = applescript
    if not os.path.exists(applescript):  # source code
        path = temp.tempfile()
        open(path, "w").write(applescript)
    args = ["osascript", path]
    return runcmd.run(args, background=background)
