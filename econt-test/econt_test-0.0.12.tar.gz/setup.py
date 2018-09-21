#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='econt_test',
    version='0.0.12',
    author='Hakan Halil',
    author_email='hhalil@melontech.com',
    description='Integrating Econt API using Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.melontech.com/melontech/econt.git',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
                      'dicttoxml~=1.7.4',
                      'lxml>4.0.0,<=4.2.4',
                      'nested-lookup~=0.1.5',
                      'requests>2.18.0>,<=2.19.1',
                      'unittest-xml~=0.2.2',
                      'xmltodict~=0.11.0',
                      'six~=1.11.0',],
)
