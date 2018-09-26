# coding: utf-8
import codecs
from os import path
from setuptools import setup, find_packages


long_description = 'stellar-base is used for accessing the stellar.org blockchain with python interfacing with a horizon instance'
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='stellar-base',
    version='0.1.9.4',
    description="""Code for managing Stellar.org blockchain transactions and accounts
                 using stellar-base in python. Allows full functionality interfacing
                 with the Horizon front end. Visit https://stellar.org for more information.""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/stellarCN/py-stellar-base/',
    license='Apache',
    author='Eno',
    author_email='appweb.cn@gmail.com',
    maintainer='antb123',
    maintainer_email='awbarker@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    keywords=['stellar.org','lumens','xlm','blockchain', 'distributed exchange', 'dex', 'stellar-core', 'horizon','sdex','trading'],
    classifiers=[
         'Development Status :: 4 - Beta',
         'Intended Audience :: Developers',
         'Intended Audience :: Financial and Insurance Industry',
         'Natural Language :: Chinese (Simplified)',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'ed25519', 'crc16', 'requests', 'SSEClient', 'numpy', 'toml', 'mnemonic'
    ]
)
