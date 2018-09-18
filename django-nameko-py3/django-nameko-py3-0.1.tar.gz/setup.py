#!/usr/bin/env python3

from setuptools import setup

setup(
    name='django-nameko-py3',
    version='0.1',
    description=' Django wrapper for nameko microservice framework(python3).',
    url='http://github.com/daimon99/django-nameko',
    author='Andrew Dunai / Daimon',
    author_email='jian.dai@gmail.com',
    license='GPLv2',
    packages=['django_nameko'],
    zip_safe=False,
    install_requires=[
        'nameko',
        'django'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
