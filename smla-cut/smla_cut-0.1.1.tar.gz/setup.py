#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 09 20 22:45:00 2018

@project: smla_info
@author : likw
@company: HuMan Ltd.,Co.
"""

from distutils.core import setup

setup(
    name="smla_cut",
    version="0.1.1",
    author="smartlands",
    author_email="info@smart-lands.com",
    keywords='Smart Lands, Chinese word segementation',
    description="Chinese text segmentation from HuMan Inc.",
    long_description="Chinese text segmentation from HuMan Inc.",
    url="https://github.com/smart-lands-com/smla-cut",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "License :: OSI Approved :: MIT License",
    ],
    packages=['smla_cut'],
    package_dir={'smla_cut':'smla_cut'},
    package_data={'smla_cut':['*.*', 'data/*', 'data/emit/*.json']},
)

