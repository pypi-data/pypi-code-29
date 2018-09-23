#!/usr/bin/env python
# encoding: utf-8

import setuptools
from setuptools import setup

#with open("README.md", "r", encoding = "utf8") as fh:
#    long_description = fh.read()

setup(name='domainadaptation',
      version='0.0.1',
      description='Domain Adaptation Tools for Python',
      #long_description=long_description,
      #long_description_content_type="text/markdown",
      url='http://domainadaptation.org',
      author='Steffen Schneider',
      author_email='steffen.schneider@tum.de',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ],
)
