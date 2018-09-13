#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'google-api-python-client>=1.7.4,<1.8.0',
    'httplib2>=0.11.3,<0.12.0',
    'requests>=2.19.1,<2.20.0',
    'oauth2client>=4.1.3,<4.2.0'
]

setup(
    name="gcf_utility_functions",
    version="0.0.1",
    author="David Fort",
    author_email="ptiger10@gmail.com",
    description="Helper functions for use with Google Cloud Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test"]),
    incude_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requires,
)
