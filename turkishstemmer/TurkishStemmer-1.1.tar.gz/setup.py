#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='TurkishStemmer',
    version='1.1',
    description='Turkish Stemmer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hanefi Önaldı',
    author_email='abdullahanefi16@gmail.com',
    url='https://github.com/hanefi/turkish-stemmer-python',
    packages=find_packages(),
    )
