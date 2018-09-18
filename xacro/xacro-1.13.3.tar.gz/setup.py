#!/usr/bin/env python
from setuptools import setup, find_packages

d = {}
d['name'] = 'xacro'
d['packages'] = ['xacro']
d['scripts'] = ['scripts/xacro']

d['version'] = '1.13.3'

setup(**d)
