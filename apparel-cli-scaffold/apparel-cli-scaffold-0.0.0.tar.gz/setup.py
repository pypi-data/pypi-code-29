#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
AUTHOR_RE = re.compile(r'''__author__ = ['"](.*)['"]''')
EMAIL_RE = re.compile(r'''__email__ = ['"](.*)['"]''')

_init = open(os.path.join(ROOT, "apparel_cli", "__init__.py")).read()


def get_version():
    return _get_re(VERSION_RE, _init)


def get_author():
    return _get_re(AUTHOR_RE, _init)


def get_email():
    return _get_re(EMAIL_RE, _init)


def _get_re(re, s):
    return re.search(s).group(1)


requires = [
    "requests >=2.19.1",
    "click >=6.7",
    "clickclick >=1.2.2",
    "click-plugins >=1.0.3",
    "stups-zign==1.1.31"
]

setup(
    name="apparel-cli-scaffold",
    version=get_version(),
    description="Apparel CLI entry point",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    author=get_author(),
    author_email=get_email(),
    url="https://github.com/apparel-cli-scaffold",
    scripts=[],
    python_requires='~=3.3',
    packages=find_packages(exclude=["tests*"]),
    package_data={},
    include_package_data=True,
    install_requires=requires,
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points="""
        [console_scripts]
        mli = apparel_cli.main:mli
        """,
)
