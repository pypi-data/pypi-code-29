import io
import os

from setuptools import setup

VERSION = '0.1'

with io.open('README.md', encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='file-permissions',
    version=VERSION,
    description='A tiny wrapper to get information about file permissions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrii Rusanov',
    author_email='andrey@rusanov.me',
    url='https://github.com/andreyrusanov/permissions',
    py_modules=['permissions'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
