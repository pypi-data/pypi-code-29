# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pysimpliroute',
    version='0.1.0',
    description='Wrapper for the SimpliRoute service API',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
    ],
    url='https://gitlab.com/dansanti/pysimpliroute',
    author='Daniel Santibáñez Polanco',
    author_email='dansanti@gmail.com',
    license='GPLV3+',
    packages=['pysimpliroute'],
    install_requires=['urllib3'],
    zip_safe=False)
