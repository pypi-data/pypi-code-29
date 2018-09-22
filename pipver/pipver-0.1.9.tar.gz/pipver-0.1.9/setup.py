#!/usr/bin/env python
# coding: utf-8

import os
import sys

from setuptools import setup

requires = [
    'gitpython',
    'colorama',
    'click'
]

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='pipver',
    version='0.1.9',
    description='Python package versioning the right way.',
    long_description=readme,
    author='John Shanahan',
    author_email='shanahan.jrs@gmail.com',
    url='https://github.com/shanahanjrs/pipver',
    include_package_data=True,
    install_requires=requires,
    scripts=['scripts/pipver'],
)
