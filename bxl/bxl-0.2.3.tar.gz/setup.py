#!/usr/bin/env python

import setuptools

# BXL is a library for interacting/communicating with XNAT's REST interface
# Based on former xnatLibrary project (2014-10-15, Jordi Huguet, Dept. Radiology AMC Amsterdam)

####################################
__author__      = 'Jordi Huguet'  ##
__dateCreated__ = '20180615'      ##
__version__     = '0.2.3'         ##
__versionDate__ = '20181002'      ##
####################################

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bxl",
    version=__version__,
    author=__author__,
    author_email="jhuguetn@gmail.com",
    description="Basic library for interacting with the REST interface of XNAT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="xnat restful api neuroimaging",
    url="https://gitlab.com/bbrc/xnat/bxl",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='MIT License',
    install_requires=[
        'requests>=2.0.0','urllib3>=1.2'
    ],
    # see here: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ]
)