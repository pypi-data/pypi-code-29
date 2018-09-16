#!/usr/bin/env python
import os
from setuptools import find_packages
import find
from public import public

# http://setuptools.readthedocs.io/en/latest/setuptools.html#metadata
# http://setuptools.readthedocs.io/en/latest/setuptools.html#options


@public
def name():
    return os.path.basename(os.getcwd()).split(".")[0].lower()


@public
def packages():
    return find_packages()


@public
def py_modules():
    result = []
    for f in os.listdir(os.getcwd()):
        name, ext = os.path.splitext(f)
        if ext == ".py" and name != "setup":  # exclude setup.py
            result.append(name)
    return result


def _readline(line):
    return line.split("#")[0].lstrip().rstrip()


def _readlines(path):
    if os.path.exists(path):
        return list(map(_readline, open(path).read().splitlines()))
    return []


@public
def install_requires():
    result = []
    files = ["install_requires.txt", "requirements.txt", "requires.txt"]
    for path in files:
        lines = _readlines(path)
        result = result + lines
    return list(sorted(filter(None, set(result))))


@public
def scripts():
    path = "scripts"
    exclude = ['.DS_Store', 'Icon\r']
    return list(filter(lambda f: os.path.basename(f) not in exclude, find.files(path)))
