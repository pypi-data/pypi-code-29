#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

if (sys.version_info.major!=3):
    raise SystemError("Python version 2 is installed. Please use Python 3.")

if (sys.platform=="linux" or sys.platform=="linux2"):
    #Check for installation type
    import distro
    if(distro.id()=="ubuntu" or distro.id()=="debian"):
        protobuf_installed = 0==os.system("sudo apt-get install -y protobuf-compiler")
        print(protobuf_installed)
        if(not protobuf_installed):
            raise SystemError("Could not install Protobuf on your system.")
        base_path = os.getcwd()
        message_installed =  0==os.system("protoc --python_out='%s' asvprotobuf/std.proto" % (base_path))
        if(not message_installed):
            raise SystemError("Could not generate protobuf implementation files.")
    #Need to add more operating systems

elif (sys.platform=="darwin"):
    #Brew installation
    brew_installed = 0==os.system("which brew")
    if (not brew_installed):
        print("Homebrew is not installed on your system, installing Homebrew.")
        brew_install = 0==os.system("/usr/bin/ruby -e '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'")
        if(not brew_install):
            raise SystemError("Cannot install Homebrew on your system.")

    protobuf_installed = 0==os.system("which protoc")
    if(not protobuf_installed):
        os.system("brew install protobuf --with-python --without-python@2")

    base_path = os.getcwd()
    message_installed =  0==os.system("protoc -I %s --python_out='%s' asvprotobuf/*.proto" % (base_path,base_path))
    if(not message_installed):
        raise SystemError("Could not generate protobuf implementation files.")

else:
    raise SystemError("This package cannot be install on Windows or Cygwin.")

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
    test_suite="tests",
)
