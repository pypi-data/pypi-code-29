#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = [
    'psycopg2',
    'sqlalchemy'
]

setup(
    name='django-dbpool',
    version='0.1.0',
    description='Postgresql + PostGIS Connection Pooling for Django.',
    long_description=open('README.rst').read(),

    # I have no idea what to write here as I just combined 3 different packages to make it work..
    # And their packages are not working..

    # author='Kenneth Reitz',
    # author_email='me@kennethreitz.com',

    url='https://github.com/chrysls/django-dbpool',
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3'
    ),
)
