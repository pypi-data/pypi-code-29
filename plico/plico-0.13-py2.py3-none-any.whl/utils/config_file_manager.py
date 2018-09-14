import appdirs
from pkg_resources import Requirement, resource_filename
import shutil
import os
from plico.utils.addtree import mkdirp

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # python 2 backport


__version__= "$Id: config_file_manager.py 50 2018-04-26 21:42:20Z lbusoni $"


class ConfigFileManager():

    def __init__(self, appName, appAuthor, pythonPackageName):
        self._appName= appName
        self._appAuthor= appAuthor
        self._packageName= pythonPackageName
        self._appdirs= appdirs.AppDirs(self._appName, self._appAuthor)


    def getConfigFilePath(self):
        confPath= os.path.join(self._appdirs.user_config_dir,
                               '%s.conf' % self._packageName)
        return confPath


    def _getConfigFilePathInPackage(self):
        return resource_filename(
            Requirement(self._packageName),
            "%s/conf/%s.conf" % (self._packageName, self._packageName))


    def doesConfigFileExists(self):
        return os.path.isfile(self.getConfigFilePath())


    def installConfigFileFromPackage(self, overwrite=False):
        if self.doesConfigFileExists() and (overwrite is False):
            return
        source= self._getConfigFilePathInPackage()
        dest= self.getConfigFilePath()
        mkdirp(os.path.dirname(self.getConfigFilePath()))
        shutil.copyfile(source, dest)
