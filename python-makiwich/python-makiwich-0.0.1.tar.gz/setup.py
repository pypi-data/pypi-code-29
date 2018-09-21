#!/usr/bin/env python

import os
import sys

from setuptools import setup

from maki import VERSION

package_name = "python-makiwich"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist")
    os.system("twine upload -r pypi dist/%s-%s.tar.gz" % (package_name, VERSION))
    sys.exit()

if sys.argv[-1] == "tag":
    os.system("git tag -a v{} -m 'tagging v{}'".format(VERSION, VERSION))
    os.system("git push && git push --tags")
    sys.exit()


setup(
    name=package_name,
    version=VERSION,
    description="Create ",
    url="https://github.com/zostera/python-makiwich",
    author="Jan Pieter Waagmeester",
    author_email="jieter@zostera.nl",
    license="ISC",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="Maki icon markers",
    packages=["maki"],
    install_requires=["xmltodict"],
    package_data={"maki": ["maki/img/*.svg", "maki/img/icons/*.svg"]},
)
