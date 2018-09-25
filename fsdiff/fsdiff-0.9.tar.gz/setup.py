#!/usr/bin/env python3

# Copyright (C) 2018 Ioannis Valasakis <code@wizofe.uk>
# Licensed under the GNU GPL-3
# The GNU Public License can be found in `/usr/share/common-licenses/GPL-3'.

from setuptools import setup
from os import path

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fsdiff',
    version='0.9',
    description='fsdiff - cli tool to compare two filesystems or images',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ioannis Valasakis',
    author_email='code@wizofe.uk',
    url='https://github.com/KanoComputing/fsdiff',
    python_requires='>=3.0',
    packages=['fsdiff'],
    scripts=['bin/fsdiff'],
    data_files=[(path.join('share', 'man', 'man1'), ['man/fsdiff.1'])],
    install_requires=[
        "colorama"
    ],
    platforms='POSIX',
    license='GNU GPL v2'
)
