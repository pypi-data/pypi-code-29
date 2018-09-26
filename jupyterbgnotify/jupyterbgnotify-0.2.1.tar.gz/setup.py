# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.rst') as r:
    readme = r.read()

with open('AUTHORS.txt') as a:
    # reSt-ify the authors list
    authors = ''
    for author in a.read().split('\n'):
        authors += '| '+author+'\n'

with open('LICENSE.txt') as l:
    license = l.read()

setup(
    name='jupyterbgnotify',
    version='0.2.1',
    description='A Jupyter Notebook %%magic for Browser Notifications of Cell Completion',
    long_description=readme+'\n\n'+authors+'\nLicense\n-------\n'+license,
    author='Benjamin Manns',
    author_email='benmanns@gmail.com',
    url='https://github.com/benmanns/jupyterbgnotify',
    license='BSD-3-Clause',
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'jupyterbgnotify': ['js/*.js']},
    install_requires=[
        'ipython',
        'jupyter'
    ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ]
)
