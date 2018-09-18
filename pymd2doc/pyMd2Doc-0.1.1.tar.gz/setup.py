#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys
 
setup(
    name="pyMd2Doc",
    version="0.1.1",
    author="Yule Meng",
    author_email="88914511@qq.com",
    description="use python convert markdown file to html doc",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/yuleMeng/pyMarkdown",
    packages=['app'],
    install_requires=[
        "Markdown"
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
)
