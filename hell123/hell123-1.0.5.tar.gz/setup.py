#!/usr/bin/env python3
import os
from setuptools import setup

from hell123.dependencies.dependencies import dependency_map
from hell123.dependencies.dependency import install_arg_complete, install_dependencies

from hell123 import __version__, __mod_name__

# this is bit ambigious thing
install_dependencies(dependency_map,verbose=True)
install_arg_complete()

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name=__mod_name__,
    version=__version__,
    description='A command line tool for media editing',
    license='MIT License',
    long_description=long_description,
    # long_description_content_type="text/markdown",
    author='Sarbjit Singh',
    author_email='srbcheema1@gmail.com',
    url="http://github.com/srbcheema1/"+__mod_name__,
    install_requires=requirements, #external packages as dependencies
    packages=[__mod_name__,__mod_name__+'.lib',__mod_name__+'.dependencies'],  #same as name of directories
    # packages=find_packages(), # provides same list, looks for __init__.py file in dir
    include_package_data=True,
    entry_points={
        'console_scripts': [__mod_name__+'='+__mod_name__+'.main:main']
    },
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
)
