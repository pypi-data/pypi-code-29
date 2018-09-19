#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 08 30 16:29:20 2018

@project: smla-cut
@author : likaiwei
@company: HuMan Ltd.,Co.
"""

# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = "smla-cut",
    version = "0.1.0",
    keywords = 'NLP,tokenizing,Chinese word segementation',
    description = "Chinese text segmentation",
    long_description = "Chinese text segmentation from HuMan Ltd.,Co.",
    license = "MIT",
    classifiers=[
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Natural Language :: Chinese (Simplified)',
      'Natural Language :: Chinese (Traditional)',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing',
      'Topic :: Text Processing :: Indexing',
      'Topic :: Text Processing :: Linguistic',
    ],

    url = "https://github.com/smart-lands-com/smla-cut",
    author = "smartlands",
    author_email = "info@smart-lands.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    package_data={'data':['/emit/*.json']}
)
