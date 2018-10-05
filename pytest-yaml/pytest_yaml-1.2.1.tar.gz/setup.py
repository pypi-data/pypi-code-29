#!/usr/bin/env python

from setuptools import setup

from pytest_yaml import __version__

setup(
    name='pytest_yaml',
    version=__version__,
    description='This plugin is used to load yaml output to your test using pytest framework.',
    long_description=open('README.md').read(),
    author='Jihad BENABRA',
    author_email='jihad_benabra@carrefour.com',
    url='https://github.com/Benabra/pytest_yaml',
    packages=['pytest_yaml'],
    install_requires=['pyyaml', 'pytest'],
    entry_points={'pytest11': ['yaml = pytest_yaml.plugin']},
    classifiers=["Framework :: Pytest"],
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='py.test pytest yaml',
)
