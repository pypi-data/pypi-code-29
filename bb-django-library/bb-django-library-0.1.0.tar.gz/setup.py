#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner >=4.0,<5dev'] if needs_pytest else []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='bb-django-library',
    version='0.1.0',
    author='Bigbox S.A.',
    author_email='innovation@bigbox.com.ar',
    description='This is an example repository for a simple Django library.',
    license='MIT',
    keywords='bigbox django python library',
    url='https://github.com/openbox/bb-django-library',
    packages=['bb_django_library'],
    setup_requires=pytest_runner,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
    ],
)
