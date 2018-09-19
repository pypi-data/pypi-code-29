#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from os import path

from setuptools import find_packages, setup


requirements = [
    'Click>=6.0',
    "pyahocorasick>=1.1.8",
]

setup_requirements = [
]

test_requirements = [
    'pyhamcrest>=1.9.0',
]


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author="Pokey Rule",
    author_email='pokey.rule@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Relabel files in order to work on them blind",
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'blind_files=blind_files.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='blind_files',
    name='blind_files',
    packages=find_packages(include=['blind_files']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pokey/blind_files',
    version='0.2.4',
    zip_safe=False,
)
