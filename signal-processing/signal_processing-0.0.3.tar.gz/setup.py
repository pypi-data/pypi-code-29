# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:42:03 2018

@author: osama
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signal_processing",
    version="0.0.3",
    author="Osama Dar",
    author_email="osamadar1996@gmail.com",
    description="This repository provides some helper functions for signal processing functions related to time series (in Python).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daroodar/TimeSeriesSignalProcessing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
