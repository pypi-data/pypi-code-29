import os
import json
from configparser import ConfigParser


class _Config:
    def to_json(self):
        return dict(
            config_type=self.config_type,
            default=self.default,
            value=self.value,
            env_var=self.env_var
        )

    @staticmethod
    def _valid_type(config_type):
        return any(
            [
                config_type == str,
                config_type == list,
                config_type == dict,
                config_type == int,
                config_type == float,
                config_type == bool
            ]
        )

    def __init__(self, config_type, default, value=None, env_var=None):
        if self._valid_type(config_type):
            self.config_type = config_type
        else:
            raise TypeError("%s is not a valid type" % config_type)
        self.default = default
        if value:
            self._value = value
        else:
            self._value = default
        self.env_var = env_var

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is self.config_type:
            self._value = value
        elif self.config_type is list or self.config_type is dict and type(value) is str:
            temp = json.loads(value)
            if type(temp) is self.config_type:
                self._value = temp
        elif self.config_type is int:
            self._value = int(value)
        elif self.config_type is float:
            self._value = float(value)
        elif self.config_type is bool:
            if type(value) is bool:
                self._value = value
            elif value.lower() == 'true':
                self._value = True
            elif value.lower() == 'false':
                self._value = False
            else:
                raise KeyError()


class EZConfig:
    __instance = None
    configuration = dict()

    def __getattribute__(self, item):
        if item != 'configuration' and item in self.configuration.keys():
            return self.configuration[item].value
        return object.__getattribute__(self, item)

    def __init__(self):
        if EZConfig.__instance is not None:
            pass
        else:
            EZConfig.__instance = self

    def register_config(self, name, config_type, default, value=None, env_var=None):
        if type(default) is not config_type:
            raise TypeError("default : %s is not type : %s" % (type(default), config_type))
        if value is not None and type(value) is not config_type:
            raise TypeError("value : %s is not type : %s" % (type(value), config_type))
        self.configuration[name] = _Config(
            config_type=config_type,
            default=default,
            value=value,
            env_var=env_var
        )

    def unregister_config(self, name):
        del self.configuration[name]

    def list_config(self):
        return list(self.configuration.keys())

    def get_config(self, name):
        return self.configuration[name].to_json()

    def set_config(self, name, value):
        self.configuration[name].value = value

    def load_config_from_env(self):
        for name, config in self.configuration.items():
            if config.env_var:
                if os.environ.get(config.env_var):
                    config.value = os.environ.get(config.env_var)

    def load_config_from_json_file(self, path):
        with open(path, 'r') as config_file:
            config = json.loads(config_file.read())
            for name, value in config.items():
                if name in self.configuration:
                    self.configuration[name].value = value

    def load_config_from_ini_file(self, path, section):
        parser = ConfigParser()
        parser.read(path)
        for name, value in parser[section].items():
            if name in self.configuration:
                self.configuration[name].value = value


ezcfg = EZConfig()
