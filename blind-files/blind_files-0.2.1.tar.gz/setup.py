#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [
    "pyahocorasick>=1.1.8",
]

test_requirements = [
    'pyhamcrest>=1.9.0',
]

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
    entry_points={
        'console_scripts': [
            'blind_files=blind_files.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='blind_files',
    name='blind_files',
    packages=find_packages(include=['blind_files']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pokey/blind_files',
    version='0.2.1',
    zip_safe=False,
)
