#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys

from getmac.getmac import __version__


long_description = """
'get-mac' has changed names and moved to 'getmac' on PyPI.
Please update your dependencies or notify the maintainer of the application.

New PyPI location: https://pypi.org/project/getmac/
"""

setup(
    name='get-mac',
    version=__version__,
    author='Christopher Goes',
    author_email='ghostofgoes@gmail.com',
    description='get-mac has changed names and moved to "getmac" on PyPI',
    long_description=long_description,  # This is what you see on PyPI page
    # PEP 566, PyPI Warehouse, setuptools>=38.6.0 make markdown possible
    long_description_content_type='text/markdown',
    url='https://github.com/GhostofGoes/getmac',
    license='MIT',
    packages=find_packages(exclude=['tests.py']),
    zip_safe=True,
    entry_points={  # These enable commandline usage of the tool
        'console_scripts': [
            'get-mac = getmac.__main__:main',
        ],
    },
    install_requires=['argparse'] if sys.version_info[:2] < (2, 7) else []
)
