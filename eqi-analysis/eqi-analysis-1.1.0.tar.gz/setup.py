#!/usr/bin/env python

from setuptools import setup, find_packages
import versioneer

install_requires = [
    'eqi-utils>=1.0.3',
    'pandas>=0.23.3',
    'cx_Oracle>=6.0b2',
    'sqlalchemy>=1.2.8',
    'alphalens-eqi>=1.1.0',
    'matplotlib>=2.2.2',
    'numpy>=1.14.5'
]

setup(
    name='eqi-analysis',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Factor analysis package for EQI project.',
    long_description=open('README.rst').read(),
    author='Jinpeng Zhang',
    author_email='jinzha098718@gmail.com',
    url='https://github.com/jinzha098718/eqi-analysis',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include='eqi_analysis.*'),
    install_requires=install_requires
)
