#!/usr/bin/env python
from setuptools import setup, find_packages
import aioipfs_api

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aioipfs-api",
    version=aioipfs_api.__version__,
    description="Python 3 async client for interacting with the IPFS HTTP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/bmuller/aioipfs-api",
    packages=find_packages(),
    install_requires=["aiohttp>=3.4.0", "yarl>=1.2.6"]
)
