#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.0.2'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-celery-oncommit',
    version=version,
    description="Celery wrapper that delays tasks until the django transaction has committed",
    long_description=long_description,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='django celery',
    author='Martin Chase',
    author_email='outofculture@gmail.com',
    url='https://gitlab.com/outofculture/django-celery-oncommit',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.11',
        'celery>=3.0',
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
