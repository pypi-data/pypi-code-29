#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
setup(
    name="ldmnqSDK",
    version="1.0.0",
    author="purecucumber",
    author_email="2894700792@qq.com",
    description="SDK to opreate 雷电模拟器",
    license="MIT",
    long_description=open('README.md', encoding='UTF-8').read(),
    url="https://coding.net/u/hhhhhg/p/ldmnqSDK/git",
    packages=['ldmnqSDK'],
    install_requires=[],
    classifiers=[
        "Natural Language :: Chinese (Simplified)",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ]
)
