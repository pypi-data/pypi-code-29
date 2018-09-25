# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


LICENSE_PATH = os.path.join(os.path.dirname(__file__), 'LICENSE')
README_PATH = os.path.join(os.path.dirname(__file__), 'readme.org')
VERSION_PATH = os.path.join(os.path.dirname(__file__), 'quasi', 'version.py')
version = {}
with open(VERSION_PATH) as fp:
    exec(fp.read(), version)

with open(README_PATH) as f:
    readme = f.read()

with open(LICENSE_PATH) as f:
    license = f.read()

requirements = [
    'sanic',
    'requests',
    'requests_cache',
]

setup(
    name='quasi',
    version=version['__version__'],
    description='Simple request wrapper',
    long_description=readme,
    author='Oliver Marks',
    author_email='oly@digitaloctave.com',
    url='https://gitlab.com/olymk2/quasi',
    license=license,
    data_files=[("readme.org", ['readme.org']), ("LICENSE", ["LICENSE"])],
    packages=find_packages(exclude=('tests', 'docs')),
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3 License',
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
      ],

    install_requires=requirements,
    setup_requires=['pytest-runner',],
    tests_require=['pytest']
)
