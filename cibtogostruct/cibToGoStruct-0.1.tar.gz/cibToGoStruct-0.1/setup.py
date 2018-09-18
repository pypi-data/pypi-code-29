#!/usr/bin/env python3

from setuptools import setup

setup(name='cibToGoStruct',
      version='0.1',
      author='Xin Liang',
      author_email='XLiang@suse.com',
      scripts=['bin/cibToGoStruct'],
      install_requires=['lxml', 'jinja2'])
