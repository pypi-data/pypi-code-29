#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

__author__ = "drewpearce <drew@caffdev.com>"
__copyright__ = "Copyright 2018, Drew Pearce"

description = 'Lego for getting a random "fact" from the Portal 2 Fact Sphere'
name = 'legos.fact_sphere'
setup(
    name=name,
    version='0.1.1',
    namespace_package=name.split('.')[:-1],
    license='GPL3',
    description=description,
    author='drewpearce',
    url='https://github.com/Legobot/' + name,
    install_requires=[
        'legobot',
        'pyyaml'
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha'
    ],
    packages=find_packages(),
    package_data={
        'legos': ['facts.yaml']
    },
    include_package_data=True
)
