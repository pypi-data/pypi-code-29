#!/usr/bin/env python
# Copyright (c) 2018, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# GNU General Public License v3.0+ (https://www.gnu.org/licenses/gpl-3.0.txt)

"""Build script for aftershocks."""

from setuptools import setup

with open('README.rst', 'r') as f:
    README = f.read()

setup(name='aftershocks',
      version='0.1.0',
      description='Plot recent earthquakes in Japan by region',
      long_description=README,
      long_description_content_type='text/x-rst',
      url='http://github.com/juseg/aftershocks',
      author='Julien Seguinot',
      author_email='seguinot@vaw.baug.ethz.ch',
      license='gpl-3.0',
      py_modules=['aftershocks'],
      install_requires=['matplotlib', 'pandas'],
      scripts=['aftershocks.py'],
      zip_safe=False)
