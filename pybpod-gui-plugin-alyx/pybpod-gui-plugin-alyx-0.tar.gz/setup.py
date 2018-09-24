#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
	name='pybpod-gui-plugin-alyx',
	version=0,
	description="""PyBpod Alyx API connectoin module""",
	author=['Sergio Copeto'],
	author_email='sergio.copeto@research.fchampalimaud.org, ricardo.ribeiro@research.fchampalimaud.org',
	license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
	url='',

	include_package_data=True,
	packages=find_packages(),

	package_data={'pybpod_alyx_module': ['resources/*.*',]}
)