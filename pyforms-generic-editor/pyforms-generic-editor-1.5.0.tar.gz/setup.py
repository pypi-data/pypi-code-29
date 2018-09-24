#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pyforms_generic_editor/__init__.py', 'r') as fd:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError('Cannot find version information')


setup(
	name='pyforms-generic-editor',
	version=version,
	description="""pyforms_generic_editor""",
	author='Ricardo Ribeiro & Carlos Mão de Ferro',
	author_email='ricardojvr@gmail.com, cajomferro@gmail.com',
	license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
	url='https://bitbucket.org/fchampalimaud/pyforms-generic-editor',

	include_package_data=True,
	packages=find_packages(),
	package_data={'pyforms_generic_editor': [
		'resources/icons/*.*',
	]
	},

	#install_requires=[],

	entry_points={
		'gui_scripts': [
			'pyfgui=pyforms_generic_editor.__main__:start',
		],
	},


)
