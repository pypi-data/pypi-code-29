#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

def _requires_from_file(filename):
	return open(filename).read().splitlines()

setup(
	name='pygrowth',
	version='0.0.4',
	url='https://github.com/growth-team/pygrowth',	
	author='GROWTH-team',
	author_email='teruaki.enoto@gmail.com',
	maintainer='Teru Enoto',
	maintainer_email='teruaki.enoto@gmail.com',
	description='Python package for public data analyses from the GROWTH collaboratoin.',
	long_description=open('README.md').read(),
	packages=find_packages(),
	#packages=find_packages(exclude=['tests*']),
	#packages=['pygrowth','pygrowth.general'],
	install_requires=['numpy'],
	#install_requires=_requires_from_file('requirements.txt'),
	license='MIT'
)
