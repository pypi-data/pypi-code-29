#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import os
import shutil

script_from_path = 'ovitoclient/ovitoclient.py'
script_to_path = 'build/_scripts/ovitoclient'
script_to_dir = os.path.dirname(script_to_path)
os.makedirs(script_to_dir, exist_ok=True)
shutil.copyfile(script_from_path, script_to_path)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Ben Lindsay",
    author_email='benjlindsay@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Ovito Client is a command-line utility with some basic rendering capabilities for trajectory files using Ovito.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ovitoclient',
    name='ovitoclient',
    packages=find_packages(include=['ovitoclient']),
    scripts=[script_to_path],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/benlindsay/ovitoclient',
    version='0.3.1',
    zip_safe=False,
)
