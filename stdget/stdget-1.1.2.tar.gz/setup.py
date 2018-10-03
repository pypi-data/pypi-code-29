"A library to capture sys.stdout and -err"

from setuptools import setup, find_packages
from os import path
from io import open
with open(path.join(path.curdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='stdget',
    version='1.1.2',
    description="A library to capture sys.stdout and -err",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CenTdemeern1/stdget',
    author='CenTdemeern1',
    author_email='timo.herngreen@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        ],
    keywords='sys std stdout stderr get stdget sys.stdout sys.stderr capture')
