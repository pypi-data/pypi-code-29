import logging
import os
import datetime


__version__= "$Id: starter_script_creator.py 31 2018-01-27 10:47:29Z lbusoni $"


class StarterScriptCreatorBase(object):

    def __init__(self):
        NOT_INITIALIZED=None
        self._binDir= NOT_INITIALIZED
        self._pythonPath= NOT_INITIALIZED
        self._configFileDest= NOT_INITIALIZED


    def _now(self):
        return datetime.datetime.now()


    def _createFoldersIfMissing(self, filename):
        if not os.path.isdir(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))


    def setInstallationBinDir(self, binDir):
        self._binDir= binDir


    def setPythonPath(self, pythonPath):
        self._pythonPath= pythonPath


    def setConfigFileDestination(self, configFileDest):
        self._configFileDest= configFileDest


    def _createAStarterScript(self,
                              destinationPath,
                              executableSrc,
                              configFileSection,
                              command='python'):
        logging.info("Creating starter script %s" % destinationPath)
        self._createFoldersIfMissing(destinationPath)
        with open(destinationPath, "w") as text_file:
            text_file.write("#!/bin/bash\n")
            text_file.write("# Auto-generated on %s - %s\n\n" % (
                str(self._now()), __version__))
            text_file.write('export PYTHONPATH="%s":$PYTHONPATH\n' %
                            self._pythonPath)
            text_file.write("%s '%s' '%s' %s\n" % (
                command,
                os.path.join(self._pythonPath, executableSrc),
                self._configFileDest,
                configFileSection))

        self._setExecutableFlag(destinationPath)


    def _setExecutableFlag(self, filePath):
        self._execute('chmod +x "%s"' % filePath)


    def _execute(self, cmd):
        logging.info(cmd)
        exitCode= os.system(cmd)
        assert os.EX_OK == exitCode, "Command '%s' must succeed" % cmd


    def installExecutables(self):
        assert False, 'method to be implemented by derived classes'
