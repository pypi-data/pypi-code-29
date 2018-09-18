#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pip.req import parse_requirements
#from pip.download import PipSession

with open('README.rst') as readme_file:
    readme = readme_file.read()

install_reqs = parse_requirements('requirements_dev.txt')
# parse_requirements() returns generator of pip.req.InstallRequirement objects
#install_reqs = parse_requirements('requirements_dev.txt', session=PipSession())

#dev_reqs = [str(ir.req) for ir in install_reqs]

requirements = [
    'requests',
]

#setup_requirements = dev_reqs

#test_requirements = dev_reqs


setup(
    name='kaze-python-rpc',
    version='1.0.0.0',
    description="A Python RPC Client for the kaze Blockchain",
    long_description=readme,
    author="Moe Sayadi",
    author_email='moe@kazesolutions.ch',
    url='https://github.com/KAZEBLOCKCHAIN/kaze-python-rpc',
    packages=find_packages(include=['kazerpc']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='kaze, python, rpc, client',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ],
    #test_suite='tests',
    #tests_require=test_requirements,
   # setup_requires=setup_requirements,
)
