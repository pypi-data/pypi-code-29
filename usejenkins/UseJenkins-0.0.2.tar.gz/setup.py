#!/local/bin/env python3
# -*- coding:utf8 -*-
# Fangbinbin

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UseJenkins",
    version="0.0.2",
    author="Fangbinbin",
    author_email="fangbinbin30@163.com",
    description="How to Use Jenkins！",
    url="https://github.com/fangbinbin30",
    py_modules = ['UseJenkins'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)