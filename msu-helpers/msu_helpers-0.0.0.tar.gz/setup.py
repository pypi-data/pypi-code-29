#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='msu_helpers',
    packages=find_packages(),
    description='Package created for the university project to store common application logic in one place.'
                'I am pretty sure that you do not need it',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='',
    url='https://github.com/Ujinjinjin/msu_helpers',
    author='ujinjinjin',
    author_email='gallkam@outlook.com ',
    keywords=['pip','msu_sqluniversity'],
)
