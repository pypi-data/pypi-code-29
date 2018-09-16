#!/usr/bin/env python
try:
    from ConfigParser import ConfigParser  # python2
except ImportError:
    from configparser import ConfigParser  # python3
from configparser2string import configparser2string
from dict2configparser import dict2configparser
from setupcfg_ import metadata, options
from setupcfg_.values import string2value, stringsdict
from public import public
from orderdict import orderdict
import write

# http://setuptools.readthedocs.io/en/latest/setuptools.html#metadata
SECTIONS = ["metadata", "options"]
# todo: add known sections


@public
class Setupcfg(dict):
    def load(self, path="setup.cfg"):
        config = ConfigParser()
        config.read(path)
        for section in config.sections():
            if section not in self:
                self[section] = dict()
            for option, value in config.items(section):
                self[section][option] = string2value(value)
        return self

    def save(self, path):
        value = self.string()
        write.write(value)
        return self

    def _configparser(self):
        data = dict(self)  # copy self
        data["metadata"] = orderdict(metadata.KEYS, self.get("metadata", {}))
        data["options"] = orderdict(options.KEYS, self.get("options", {}))
        for key, value in data.items():
            data[key] = stringsdict(value)  # python types to setup.cfg string values
        data = orderdict(SECTIONS, data)  # sort sections [metadata], [options], ...
        return dict2configparser(data)

    def string(self):
        return configparser2string(self._configparser())

    def __getattr__(self, attr):
        if attr in self:
            return self[attr]

    def __setitem__(self, key, value):
        if not isinstance(value, dict):
            raise ValueError("'%s' is not dict" % key)
        super(type(self), self).__setitem__(key, value)

    def __str__(self):
        return self.string()
