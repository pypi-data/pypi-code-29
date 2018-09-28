#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prwm",
    version="0.0.1",
    author="Alexey Shildyakov",
    author_email="ashl1future@gmail.com",
    description="Packed Raw WebGL Model (PRWM) exporter in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashl1/PRWM/tree/master/implementations/prwm-python",
    packages=setuptools.find_packages(),
    classifiers=(
	"Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Topic :: Multimedia :: Graphics :: 3D Rendering",
	"Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ),
    requires=["enum34"],
)
