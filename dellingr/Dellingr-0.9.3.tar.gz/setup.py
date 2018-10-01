#!/usr/bin/env python

from setuptools import setup, find_packages
import re

# Imports version number
VERSIONFILE = "Dellingr/__version.py"
verstrline = open(VERSIONFILE, "rt").read()
verRegex = r"^__version__ = ['\"]([^'\"]*)['\"]"
currentVer = re.search(verRegex, verstrline, re.M)
if currentVer:
    version = currentVer.group(1)
else:
    version = "Unknown"

# Read in the README for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Dellingr',
    version=version,
    description='Error supression and variant calling pipeline for Second-Generation sequencing data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Christopher Rushton',
    author_email='ckrushto@sfu.ca',
    include_package_data=True,
    packages=["Dellingr"],
    url='https://github.com/morinlab/Dellingr',
    classifiers=[
       "Programming Language :: Python :: 3",
       "Operating System :: Unix",
       "Topic :: Scientific/Engineering :: Bio-Informatics",
       "License :: OSI Approved :: GNU Affero General Public License v3"
       ],
    setup_requires=["numpy"],
    python_requires='>=3.4, <3.7',
    install_requires=[
        "sortedcontainers",
        "scipy",
        "configobj",
        "scikit-bio",
        "pyfaidx",
        "pysam",
        "packaging",
        "sklearn",
        "fisher"
        ],
    download_url="https://github.com/morinlab/Dellingr/dist/Dellingr-0.9.3.tar.gz",
    scripts=["bin/dellingr"],
    package_data = {"Dellingr": ["LICENSE.txt", "README.md", "etc/default_filter.pkl"]},
    zip_safe = False,
    project_urls={
        "Source": "https://github.com/morinlab/Dellingr",
        "Documentation": "https://dellingr.readthedocs.io/en/latest/"
        }
)

