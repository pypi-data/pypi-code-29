#!/usr/bin/env python
# coding: utf-8

import os
import sys

from setuptools import setup

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

requires = [
    'gitpython',
    'click'
]

setup(
    name='pipver',
    version='0.1.4',
    description='Python package versioning the right way.',
    author='John Shanahan',
    author_email='shanahan.jrs@gmail.com',
    url='https://github.com/shanahanjrs/pipver',
    include_package_data=True,
    install_requires=requires,
    scripts=['scripts/pipver'],
)
