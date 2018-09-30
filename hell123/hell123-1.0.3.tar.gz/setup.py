#!/usr/bin/env python3
import os
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='hell123',
    version='1.0.3',
    description='A test for making projects',
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sarbjit Singh',
    author_email='srbcheema2@gmail.com',
    install_requires=[], #external packages as dependencies
    packages=['hell123'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['hell123=hell123.main:main']
    },
)
