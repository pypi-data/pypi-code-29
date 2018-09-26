# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 07:16:18 2017

@author: twagner
"""

### imports from ##############################################################
from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS

###############################################################################
class SingleInstance:
    """ Limits application to single instance """

    def __init__(self, name):
        self.mutex = CreateMutex(None, False, name)
        self.lasterror = GetLastError()
    
    def alreadyRunning(self):
        return (self.lasterror == ERROR_ALREADY_EXISTS)
        
    def __del__(self):
        if self.mutex:
            CloseHandle(self.mutex)

###############################################################################
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)

    # do this at beginnig of your application
    myapp = SingleInstance('myapp')
    
    # check is another instance of same program running
    if myapp.alreadyRunning():
        print("Another instance of this program is already running")
        sys.exit(0)

    # not running, safe to continue...
    print("No another instance is running, can continue here")
    sys.exit(app.exec_())
