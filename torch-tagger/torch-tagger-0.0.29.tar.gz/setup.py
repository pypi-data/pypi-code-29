#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: InfinityFuture
# Mail: infinityfuture@foxmail.com
# Created Time: 2018-09-06 10:00:00
#############################################

import os
from setuptools import setup, find_packages

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if not on_rtd:
    install_requires = [
        'torch', 'tqdm', 'scikit-learn', 'numpy', 'scipy'
    ]
else:
    install_requires = []

version = os.path.join(
    os.path.realpath(os.path.dirname(__file__)),
    'version.txt'
)

setup(
    name = 'torch-tagger',
    version = open(version, 'r').read().strip(),
    keywords = ('pip', 'pytorch', 'NER', 'tagger'),
    description = 'NLP tool',
    long_description = 'NLP tool, NER, POS',
    license = 'MIT Licence',

    url = 'https://github.com/infinity-future/torch-tagger',
    author = 'infinityfuture',
    author_email = 'infinityfuture@foxmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = install_requires
)
