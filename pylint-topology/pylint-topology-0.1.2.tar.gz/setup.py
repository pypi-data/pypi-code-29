# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pylint-topology',
    version='0.1.2',
    description='check module topology in pylint',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/pylint_topology',
    license='GPLv2',
    packages=['pylint_topology'],
    install_requires=['pylint>=2.0'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
