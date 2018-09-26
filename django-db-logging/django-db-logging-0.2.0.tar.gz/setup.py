#!/usr/bin/env python
import ast
import codecs
import os
import re
import subprocess
from distutils.errors import DistutilsError

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as BaseSDistCommand

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))
init = os.path.join(ROOT, 'src', 'django_db_logging', '__init__.py')

_version_re = re.compile(r'__version__\s+=\s+(.*)')
_name_re = re.compile(r'NAME\s+=\s+(.*)')

with open(init, 'rb') as f:
    content = f.read().decode('utf-8')
    version = str(ast.literal_eval(_version_re.search(content).group(1)))
    name = str(ast.literal_eval(_name_re.search(content).group(1)))

tests_requires = ['django-webtest',
                  'pytest',
                  'pytest-coverage',
                  'pytest-django',
                  'pytest-echo',
                  'pytest-pythonpath',
                  'tox',
                  ]
setup(
    name=name,
    version=version,
    url='https://github.com/saxix/django-db-logging',
    author='Stefano Apostolico',
    author_email='s.apostolico@gmail.com',
    license="MIT",
    description='Database logging handler with Django integration',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=["admin-extra-urls"],
    tests_require=tests_requires,
    extras_require={
        'test': tests_requires,
    },
    platforms=['linux'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers'
    ]
)
