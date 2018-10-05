import os
import errno
import sys

import pkg_resources


class Util(object):
    def __init__(self):
        self.className = 'Util'



    def getAbsPath(self, filename):
        absPath =  os.path.abspath(filename) # This is your Project Root
        return absPath

    def getCurDirPath(self, filename):
        absPath = self.getAbsPath(filename)
        curDirPath = os.path.dirname(absPath)
        return curDirPath

    def getRootPath(self, modulename):
        mainModule = pkg_resources.resource_filename(modulename,'')
        mainPath = self.getAbsPath(mainModule + os.path.sep + ".." )

        return self.getAbsPath(mainPath)

    def makeDir(self, path):
        if os.path.isfile(path) :
            directory = os.path.dirname(path)
        else :
            directory = path
        if not os.path.exists(directory):
            os.makedirs(directory)

    def rreplace(self, s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)