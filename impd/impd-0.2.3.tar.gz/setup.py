#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='impd',
    version='0.2.3',
    description='A simple Gtk interface for MPD.',
    author='Steven J. Core',
    license='GPL 3.0',
    packages=['impd'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'musicbrainzngs',
        'requests',
        'python-mpd2',
    ],
    entry_points={
        'console_scripts': [
            'impd = impd.impd:main'
        ]
    }
)
