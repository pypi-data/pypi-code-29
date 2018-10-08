#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008-2018 Sergey Poznyakoff
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from codecs import open

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='releaselogparser',
      version='1.0.1',
      author='Sergey Poznyakoff',
      author_email='gray@gnu.org',
      url='http://git.gnu.org.ua/cgit/releaselogparser.git/',
      packages = find_packages(exclude=['contrib', 'docs',
                                        'tests', 'testdata']),
      scripts=['bin/releaselog'],
      license='GPL License',
      description='Release log parser.',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      platforms=['any'],
      test_suite='tests',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General'
      ],
      keywords = 'release log history changes news',
)
