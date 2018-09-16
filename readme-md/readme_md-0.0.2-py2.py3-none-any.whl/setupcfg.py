#!/usr/bin/env python
import os
import sys
from envdict import envdict
from public import public
from slicedict import slicedict
from setupcfg_ import default, metadata, options
from setupcfg_.cfg import Setupcfg


@public
def get(section, option=None, default=None):
    cfg = Setupcfg().load("setup.cfg")
    if not option:
        return cfg.get(section, {})  # section dict. {} if not exists
    return cfg.get(section, {}).get(option, default)  # option value or default value


@public
def set(section, option, value):
    raise NotImplementedError


def _env_dict():
    # todo: multiline environment variables
    return envdict(metadata.KEYS + options.KEYS)


def _default_dict():
    return dict(
        install_requires=default.install_requires(),
        name=default.name(),
        packages=default.packages(),
        py_modules=default.py_modules(),
        scripts=default.scripts()
    )


def _merge_dicts(d1, d2):
    return dict(list(d1.items()) + list(d2.items()))  # python 2/3 compatible


def _cli_setupcfg():
    # default values + environment variables
    data = _merge_dicts(_default_dict(), _env_dict())
    return Setupcfg(
        metadata=slicedict(data, metadata.KEYS),
        options=slicedict(data, options.KEYS)
    )


USAGE = 'usage: python -m %s' % __file__.split("/")[-1].split(".")[0]


def _cli():
    if not os.path.exists("setup.py"):
        raise OSError("%s/setup.py not exists" % os.getcwd())
    cfg = _cli_setupcfg()
    print(str(cfg))


if __name__ == "__main__":
    if sys.argv[-1] == "--help":
        print(USAGE)
        sys.exit(0)
    _cli()
