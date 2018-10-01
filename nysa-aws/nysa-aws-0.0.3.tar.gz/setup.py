"""
    AWS ECS tools
"""
import os
import sys
from setuptools import find_packages, setup
from nysa_aws import VERSION
from setuptools.command.install import install

dependencies = [
    'botocore>=1.10.9',
    'boto3>=1.7.9',
    'jsonmerge>=1.5.0',
    'jsondiff>=1.1.2'
]

classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='nysa-aws',
    version=VERSION,
    url='https://github.com/fernandosure/nysa-aws',
    download_url='https://github.com/fernandosure/nysa-aws/archive/%s.tar.gz' % VERSION,
    license='MIT',
    author='Fernando Sure',
    author_email='fernandosure@gmail.com',
    description='Ready to use library for interacting with AWS ECS',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    keywords=['ECS', 'AWS'],
    tests_require=[
        'mock',
        'pytest',
        'pytest-flake8',
        'pytest-mock',
        'coverage'
    ],
    classifiers=classifiers
)
