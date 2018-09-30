# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

__author__ = 'nebulas.io'
__date__ = '2018/09/30'


setup(
    name='nebnr',
    version='1.0.1',
    description='Nebulas Rank SDK',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='nebulas rank nr nebnr nas',
    author='nebulas.io',
    author_email='nebnr@nebulas.io',
    url='https://github.com/nebulasio/nebnr',
    license='Apache Licence 2.0',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
)
