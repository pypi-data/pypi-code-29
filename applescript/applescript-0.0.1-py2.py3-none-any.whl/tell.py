#!/usr/bin/env python
import only
from public import public
import runcmd
import temp


def _tempfile(content):
    path = temp.tempfile()
    open(path, "w").write(content)
    return path


@only.osx
@public
def app(appname, applescript, background=False):
    code = """tell application "%s"
    %s
end tell
""" % (appname, applescript)
    path = _tempfile(code)
    args = ["osascript", path]
    return runcmd.run(args, background=background)
