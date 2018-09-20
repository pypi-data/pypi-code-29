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
    name="smla_info",
    version="0.1.2",
    author="smartlands",
    author_email="info@smart-lands.com",
    keywords='Smart Lands, HuMan',
    description="Infomation about Smart Lands.",
    long_description="Infomation about Smart Lands.",
    url="https://github.com/smart-lands-com/smla-info",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "License :: OSI Approved :: MIT License",
    ],
    packages=['smla_info'],
    package_dir={'smla_info':'smla_info'},
    package_data={'smla_info':['*.*']},
)

