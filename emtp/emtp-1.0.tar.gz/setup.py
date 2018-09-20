#!/usr/bin/env python

import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='emtp',
    version='1.0',
    packages=find_packages(),

    author='Yeison Cardona',
    author_email='yencardonaal@unal.edu.co',
    maintainer='Yeison Cardona',
    maintainer_email='yencardonaal@unal.edu.co',

    # url = '',
    download_url='https://bitbucket.org/GREDyP/emtp/',

    install_requires=['numpy',
                      'pandas',
                      ],

    include_package_data=True,
    license='BSD License',
    description="EMTP is a software package for .",

    classifiers=[

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)
