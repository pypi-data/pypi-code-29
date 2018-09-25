#!/usr/bin/env python
from setuptools import setup

VERSION = '1.5.1'
BASE_URL = 'https://bitbucket.org/lskibinski/et3'

setup(**{
    'name': 'et3',
    'version': VERSION,
    'description': 'Simple library for Extracting and Transforming data, third incarnation.',
    'url': BASE_URL,
    'download_url': BASE_URL + '/get/' + VERSION + '.tar.gz',
    'license': 'GPLv3',
    'author': 'Luke',
    'author_email': 'lsh-0@users.noreply.github.com',
    'test_suite': 'et3.tests',
    'packages': ['et3'],
    'install_requires': [], # see install.sh and requirements-dev.txt for local development
    'platforms': ['any'],
    'classifiers': [
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ]
})
