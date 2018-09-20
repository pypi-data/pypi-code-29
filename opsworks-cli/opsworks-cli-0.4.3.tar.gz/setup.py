from setuptools import setup, find_packages
from codecs import open
from os import path
from io import open
import modules

setup(
    name='opsworks-cli',
    description='A simple python module to work with aws opsworks',
    url='https://github.com/chaturanga50/opsworks-cli',
    author='Chathuranga Abeyrathna',
    author_email='chaturanga50@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    version='0.4.3',
    install_requires=[
        'boto3'
    ],
    scripts=['opsworks-cli']
)
