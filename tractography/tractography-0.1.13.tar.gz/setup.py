#!/usr/bin/python3.6
from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tractography",
    version="0.1.13",
    author="Mohammed Abdelgadir",
    description="The package deals with brain bundles images",
    long_description=long_description,
    url="https://weekmo.github.io/Tractography/",
    package_dir={'src': 'tractography'},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'plyfile',
        'numpy',
        'dipy',
        'open3d-official'
    ]
)
"""
sleep(2)
remove("README.md")
"""