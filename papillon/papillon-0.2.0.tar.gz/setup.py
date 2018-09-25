#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: domenico.somma@glasgow.ac.uk
"""

from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='papillon',
    version='0.2.0',
    py_modules=['papillon'],
    description='A Python module to read and plot (cuffdiff) Galaxy RNA-seq data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Domenico Somma',
    author_email='domenico.somma@glasgow.ac.uk',
    license='Mozilla Public License 2.0',
    url='https://github.com/domenico-somma/Papillon/',
    python_requires='>=3.3, <4',
    install_requires=[
        "pandas >= 0.23",
        "Seaborn >= 0.8.1",
    ],
)
