#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    return '0.1.0'

version = get_version()


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-riotjs-helper',
    version=version,
    description="""A small, rudimentary helper app for RiotJS integration into django projects.""",
    long_description=readme + '\n\n' + history,
    author='Thomas Weholt',
    author_email='thomas@weholt.org',
    url='https://github.com/weholt/django-riotjs-helper',
    packages=[
        'riotjs_helper',
    ],
    include_package_data=True,
    install_requires=['django'],
    license="MIT",
    zip_safe=False,
    keywords='django-riotjs-helper',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
