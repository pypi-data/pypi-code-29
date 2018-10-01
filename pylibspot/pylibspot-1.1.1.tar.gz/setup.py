#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: asr
"""

from setuptools import setup
#import os

## working directory
#WD = os.path.dirname(os.path.realpath(__file__))
#INCLUDE = os.path.join(WD, 'include/')
#SRC = os.path.join(WD, 'src/')
#
## the external library (libspot)
#libspot = Extension('libspot',
#                    include_dirs = [INCLUDE],
#                    sources = [os.path.join(SRC, x) for x in os.listdir(SRC)])

setup(name = 'pylibspot',
      version = '1.1.1',
      author = "Alban Siffer",
      maintainer = "Alban Siffer",
      author_email = "alban.siffer@irisa.fr",
      maintainer_email = "alban.siffer@irisa.fr",
      url = "https://asiffer.github.io/libspot/",
      license = 'GPL-3',
      py_modules = ['pylibspot'],
      description = 'PyPI version of the python3 bindings to libspot',
      long_description = 'Originally, libspot and its python bindings are available\
      through debian packages (libspot and python3-libspot on ppa:asiffer/libspot. \
      However, to build python applications above libspot, it is more convenient \
      to use only pip to manage the dependencies')

