#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requisites = []

setup(
    name='readthecode',
    version='0.1.0',
    description='You read the doc, now better read the code',
    long_description=open('README.rst').read(),
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/readthecode',
    license='MIT',
    classifiers=[
        'Environment :: Console',
    ],
    entry_points={
        'console_scripts': [
            'readthecode=main:cli',
            'rtc=main:cli',
        ],
    },
)
