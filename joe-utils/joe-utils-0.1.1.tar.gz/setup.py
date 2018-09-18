#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Notes
# * Pypi Classifiers
#   - https://pypi.python.org/pypi?%3Aaction=list_classifiers
"""Joefuncs - A collection of reusable Python3 functions by Joe Flack
(joeflack4@gmail.com).
"""
from setuptools import setup, find_packages


setup(
    name='joe-utils',
    version='0.1.1',
    author='Joe Flack',
    author_email='joeflack4@gmail.com',
    description=('Joe Utils - A collection of reusable Python3 utilities by '
                 'Joe Flack (joeflack4@gmail.com).'),
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[],
    tests_require=[],
    url='http://www.joeflack.net/',
    keywords=['joeflack4', 'utilities'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Environment :: Other Environment',
        'Environment :: Win32 (MS Windows)',
        'Environment :: MacOS X',
        'Environment :: Plugins',
    ]
)
