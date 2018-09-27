# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

VERSION = '0.3.8'

setup(
    name='kamonohashi-cli',
    version=VERSION,
    description='KAMONOHASHI Command Line Interface',
    long_description='Python command line interface for KAMONOHASHI https://kamonohashi.ai/',
    author='NS Solutions Corporation',
    author_email='kamonohashi-support@jp.nssol.nssmc.com',
    url='https://github.com/KAMONOHASHI/kamonohashi-cli',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'six >= 1.10',
        'kamonohashi-sdk == 0.3.6',
    ],
    entry_points={
        'console_scripts': ['kqi = cli.kqi:kqi_main']
    },
)
