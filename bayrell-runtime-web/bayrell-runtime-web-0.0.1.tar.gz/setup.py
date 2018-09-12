#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname

PACKAGE = "RuntimeWeb"
about = __import__(PACKAGE)


setup(
	name = about.__name__,
	version = about.__version__,
	description = about.__description__,
	long_description = open(join(dirname(__file__), 'README.rst')).read(),
	author = about.__author__,
	author_email = about.__email__,
	license = about.__license__,
	url = about.__url__,
	packages=find_packages(),
	include_package_data = True,
	scripts=[
		#'scripts/bayrell'
	],
	install_requires=[
	],
	classifiers=[
		'Development Status :: 1 - Planning',
		'Environment :: Console',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.5',
		'Topic :: Internet',
		'Topic :: Software Development :: Interpreters',
		'Topic :: Software Development :: Libraries',
	],
)