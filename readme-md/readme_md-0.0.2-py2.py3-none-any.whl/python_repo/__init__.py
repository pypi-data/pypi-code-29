#!/usr/bin/env python
import os
from config2dict import config2dict
import setupcfg
import find
from public import public


@public
class Repo:
    def __init__(self, path=None):
        if not path:
            path = os.getcwd()
        for filename in ["setup.cfg", "setup.py"]:
            f = os.path.join(path, filename)
            if not os.path.exists(f):
                raise OSError("%s NOT EXISTS" % f)
        self.path = path
        self.files = find.files(path)

    @property
    def basename(self):
        return os.path.basename(self.path)

    @property
    def metadata(self):
        path = os.path.join(self.path, "setup.cfg")
        return setupcfg.get("metadata", {})

    @property
    def options(self):
        path = os.path.join(self.path, "setup.cfg")
        return setupcfg.get("options", {})

    @property
    def name(self):
        return self.metadata.get("name")

    @property
    def version(self):
        return self.metadata.get("version", "")

    @property
    def keywords(self):
        return self.metadata.get("keywords", "")

    @property
    def platforms(self):
        return self.metadata.get("platforms", "")

    @property
    def classifiers(self):
        value = self.metadata.get("classifiers", "")
        if "file: " in value:
            relpath = value.split(": ")[1]
            path = os.path.join(self.path, relpath)
            value = open(path).read()
        return value.splitlines()

    @property
    def packages(self):
        return self.options.get("packages", [])

    @property
    def py_modules(self):
        return self.options.get("py_modules", [])

    @property
    def scripts(self):
        return self.options.get("scripts", [])

    def __str__(self):
        return "<Repo %s>" % self.path
