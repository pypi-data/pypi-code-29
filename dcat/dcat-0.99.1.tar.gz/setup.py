#!/usr/bin/env python

from distutils.core import setup

setup(name='dcat',
      version='0.99.1',
      description='Data Cataloging Service',
      author='Shiv Deepak',
      author_email='shiv@hackerrank.com',
      url='http://dcat-docs.s3-website-us-east-1.amazonaws.com/',
      packages=['dcat'],
      scripts=['bin/dcat'],
      install_requires=['requests', 'tabulate', 'termcolor']
     )
