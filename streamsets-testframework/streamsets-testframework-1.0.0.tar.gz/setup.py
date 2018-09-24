#!/usr/bin/env python
# Copyright 2018 StreamSets Inc.

"""The setup script."""

import os
from setuptools import setup

requirements = [
    'colorlog',
    'docker',
    'streamsets',
]

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'streamsets', 'testframework', '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name='streamsets-testframework',
    version=about['__version__'],
    description='A set of tools and libraries that enables developers to write tests for StreamSets products',
    author='StreamSets, Inc.',
    author_email='eng-productivity@streamsets.com',
    packages=['streamsets.testframework.cli'],
    py_modules=['streamsets.testframework.__version__'],
    entry_points={'console_scripts': ['stf = streamsets.testframework.cli:main']},
    install_requires=requirements,
    zip_safe=False,
    keywords='streamsets testframework',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
