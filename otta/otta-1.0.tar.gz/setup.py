#!/usr/bin/env python3

from setuptools import setup

readme = open('README.md').read()

setup(
    name = 'otta',
    packages = ['otta'],
    install_requires = [
      'pyyaml',
      'jsonschema',
      'termcolor'
    ],
    version = '1.0',
    description = 'Multi-file compose/stack helper',
    long_description = readme,
    long_description_content_type='text/markdown',
    author = 'Wolphin',
    author_email = 'wolphin@wolph.in',
    url = 'https://gitlab.com/q_wolphin/otta',
    py_modules = ['otta'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'otta=otta:otta',
            'skara=otta:skara',
            'kumla=otta:kumla',
        ]
    },
)
