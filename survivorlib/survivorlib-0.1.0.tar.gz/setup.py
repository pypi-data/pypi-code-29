#!/usr/bin/env python3

from setuptools import setup, find_packages
import survivorlib

setup(
    name = 'survivorlib',
    description = survivorlib.__doc__.strip(),
    url = 'https://github.com/nul-one/survivorlib',
    download_url = 'https://github.com/nul-one/survivorlib/archive/'+survivorlib.__version__+'.tar.gz',
    version = survivorlib.__version__,
    author = survivorlib.__author__,
    author_email = survivorlib.__author_email__,
    license = survivorlib.__licence__,
    packages = [ 'survivorlib' ],
    entry_points={ 
        'console_scripts': [
            'survivorlib=survivorlib.__main__:main',
        ],
    },
    install_requires = [
        'requests>=2.9.1,<3.0',
        'xmltodict>=0.11.0,<1.0',
        'tqdm>=4.26.0,<5.0',
    ],
    python_requires=">=3.4.6",
)

