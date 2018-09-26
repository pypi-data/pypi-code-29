# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:05:33 2016

@author: twagner
"""

### imports ###################################################################
import logging
import re
import subprocess

### imports from ##############################################################
from ctypes import c_char_p
from ctypes import windll

### loging ####################################################################
logger = logging.getLogger('windows_desktop')
logger.addHandler(logging.NullHandler())

###############################################################################
def focusExternalWindow(windowname, windowPath = None):
    """
    Searches an external window by name and tries to focus it.
    """

    logger = logging.getLogger('windows_desktop')
    logger.debug("Focus external window")

    # Get handle
    hnd = windll.user32.FindWindowA(None, c_char_p(windowname.encode()))

    result = 0

    if hnd == 0:
        # If there is no Window, try to start it
        if windowPath is not None:
            # Extract directory path from complete path
            pathSearch = re.search(r'^.*\\', windowPath)

            if pathSearch is None:
                pathDir = None
            else:
                pathDir = pathSearch.group(0)

            subprocess.Popen(windowPath, cwd=pathDir)
    else:
        # Raise window
        # wndCmd = 10 # SW_SHOWNORMAL
        # wndCmd = 10 # SW_SHOWDEFAULT
        wndCmd = 9 # SW_SHOWRESTORE
        # self.showMinimized()
        windll.user32.ShowWindow(hnd, wndCmd)
        windll.user32.SetFocus(hnd)
        windll.user32.SetForegroundWindow(hnd)
        windll.user32.SetActiveWindow(hnd)

        result = 1

    return result
