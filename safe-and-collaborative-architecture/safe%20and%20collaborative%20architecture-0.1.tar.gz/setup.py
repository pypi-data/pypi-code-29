#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = None
with open('sca/__init__.py', 'r') as fd:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
if not version: raise RuntimeError('Cannot find version information')

setup(
	name='safe and collaborative architecture',
	version=version,
	description="""This library implements the safe & collaborative architecture.""",
	author=['Ricardo Ribeiro'],
	author_email='ricardojvr@gmail.com',
	url='https://bitbucket.org/fchampalimaud/safe-collaborative-architecture',
	include_package_data=True,
	packages=find_packages(exclude=['docs']),
)