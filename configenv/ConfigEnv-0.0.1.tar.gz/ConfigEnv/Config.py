import os
import json
import configparser

from .FileFormatException import FileFormatException

class Config():
    """docstring for ConfigJsonEnv."""

    def __init__(self, file = None):
        self._config = dict()
        self._configCache = dict()
        if file is not None:
            self.addFile(file)

    def addFile(self,file):
        if file.endswith('.json') :
            with open(file, 'r') as f:
                fileContent = json.load(f)
        elif file.endswith('.ini') :
            fileContent = configparser.ConfigParser()
            fileContent.read(file)
        else :
            raise FileFormatException()
        self._config = {**self._config, **fileContent}

    def get(self,path):
        if path in self._configCache:
            return self._configCache[path]
        else :
            return self._findConfig(path)

    def _findConfig(self,path):
        splited = path.split("_")
        if path in os.environ:
            config = os.environ[path]
        else :
            config = self._recursiveRoute(self._config,splited)
        self._setCache(path,config)
        return config

    def _setCache(self,path,config):
        self._configCache[path] = config

    def _recursiveRoute(self,context,left):
        search = ""
        for index in range(len(left)):
            search += left.pop(0) if len(search) == 0 else "_"+left.pop(0)
            if search in context and isinstance(context[search],dict):
                return self._recursiveRoute(context[search],left)
            elif search in context:
                return context[search]
