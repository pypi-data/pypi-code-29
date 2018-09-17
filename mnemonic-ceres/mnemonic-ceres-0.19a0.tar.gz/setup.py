#!/usr/bin/env python
from setuptools import setup

setup(
    name='mnemonic-ceres',
    version='0.19a',
    author='Bitcoin TREZOR',
    author_email='zhao6217@gmail.com',
    description='Implementation of Bitcoin BIP-0039',
    url='https://github.com/PetersonZhao/python-mnemonic',
    packages=['mnemonic', ],
    package_data={'mnemonic': ['wordlist/*.txt']},
    zip_safe=False,
    install_requires=['pbkdf2'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
)
