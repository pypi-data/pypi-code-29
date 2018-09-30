#!/usr/bin/env python

from setuptools import setup

from pytest_expectr import __version__

setup(
    name='pytest_expectr',
    version=__version__,
    description='This plugin is used to expect multiple assert using pytest framework.',
    long_description=open('README.md').read(),
    author='Jihad BENABRA',
    author_email='jihadbenabra@gmail.com',
    url='https://github.com/Benabra/pytest_expectr',
    packages=['pytest_expectr'],
    install_requires=['pytest>=2.4.2'],
    setup_requires=['setuptools_scm'],
    entry_points={'pytest11': ['expect = pytest_expectr.plugin']},
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='py.test pytest json variables',
    classifiers=["Framework :: Pytest"]
)
