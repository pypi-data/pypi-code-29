#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('loggingbootstrap/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='logging-bootstrap',
    version=version,
    description="""Library to provide simple methods to bootstrap logger with default settings.""",
    author='Carlos Mão de Ferro',
    author_email='cajomferro@gmail.com',
    license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
    url='https://bitbucket.org/fchampalimaud/logging-bootstrap',

    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports', 'build_settings'])
)
