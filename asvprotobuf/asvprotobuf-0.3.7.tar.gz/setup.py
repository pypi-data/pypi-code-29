#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

if (sys.version_info.major!=3):
    raise SystemError("Python version 2 is installed. Please use Python 3.")

if (sys.platform=="linux" or sys.platform=="linux2"):
    if(sys.maxsize>2**32):
        url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_32.zip"
    else:
        url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip"

elif (sys.platform=="darwin"):
    if(sys.maxsize>2**32):
        url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-osx-x86_32.zip"
    else:
        url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-osx-x86_64.zip"

else:
    raise SystemError("This package cannot be install on Windows or Cygwin.")

#Compilter download if OS is Linux or OSX
if(sys.platform in ["linux", "linux2", "darwin"]) and sys.argv[-1]!="test":
    os.system("curl -L %s -o protoc.zip --silent" % (url))
    os.system("unzip -q protoc.zip")
    os.system("./bin/protoc --python_out='%s' asvprotobuf/*.proto" % (os.getcwd()))
    os.system("rm -r bin/ include/ readme.txt protoc.zip")


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

readme = open("README.md", "r").read()

import asvprotobuf
version = asvprotobuf.__version__

setup(
    name="asvprotobuf",
    version=version,
    description="ASV API for using protobuf for serialization and deserialization of objects for Inter Process Communication",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Akash Purandare",
    author_email="akash.p1997@gmail.com",
    url="https://github.com/akashp1997/asvprotobuf",
    packages=["asvprotobuf"],
    include_package_data=True,
    install_requires=["protobuf>=3.6.1"],
    license="BSD-3-Clause",
    zip_safe=True,
    keywords="asvprotobuf",
)
