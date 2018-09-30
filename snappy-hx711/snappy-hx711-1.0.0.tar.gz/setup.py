#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='snappy-hx711',
    description="Synapse SNAPpy library for HX711 Load Cell Amplifier/ADC",
    long_description=readme(),
    maintainer='Tyler Crumpton',
    maintainer_email='tyler.crumpton@gmail.com',
    url='https://github.com/tylercrumpton/snappy-hx711',
    packages=['snappy_hx711'],
    setup_requires=['vcversioner'],
    vcversioner={
        'version_module_paths': ['snappy_hx711/_version.py'],
    },
)