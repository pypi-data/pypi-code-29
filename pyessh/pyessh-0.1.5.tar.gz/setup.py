#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (
    name='pyessh',
    packages=['pyessh'],
    version='0.1.5',
    description='A tool for easy to execute commands at multiserver',
    long_description=open('README.md').read(),
    author='leviathan1995',
    author_email='leviathan0992@gmail.com',
    url='https://github.com/Leviathan1995/pyessh',
    license='MIT',
    install_requires=[
        'paramiko',
        'plumbum',
        'prompt_toolkit',
    ],
    entry_points={
        'console_scripts': [
            'pyessh = pyessh.pyessh:Pyessh.run'
        ]
    },
    include_package_data=True,
    data_files=[('/usr/local/', ['pyessh.conf'])]
)
