#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import kill
import pgrep
from public import public
import mac_open
import mac_slideshow.path
import mac_slideshow.style
import runcmd


SAVER = "/System/Library/Frameworks/ScreenSaver.framework/Resources/iLifeSlideshows.saver"
EXECUTABLE = "/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine"  # High Sierra+
APP = "/System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app"  # Sierra or lower


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


@public
def pid():
    pids = pgrep.pgrep("ScreenSaverEngine")
    if pids:
        return pids[0]


@public
def enabled():
    args = ["defaults", "-currentHost", "read", "com.apple.screensaver", "moduleDict"]
    return "iLifeSlideshow" in runcmd.run(args).out


@public
def enable():
    if enabled():
        return
    args = ["defaults", "-currentHost", "write", "com.apple.screensaver", "moduleDict", "-dict", "moduleName", "iLifeSlideshow", "path", SAVER, "type", "0"]
    runcmd.run(args)
    runcmd.run(["killall", "cfprefsd", "System Preferences"])


@public
def start(path=None):
    if path:
        mac_slideshow.path.write(_fullpath(path))
    enable()
    if os.path.exists(EXECUTABLE):
        runcmd.run([EXECUTABLE])
    else:
        mac_open.app(APP)


@public
def stop():
    _pid = pid()
    if _pid:
        kill.kill(_pid)
