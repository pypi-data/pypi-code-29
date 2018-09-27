#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Wind Project",
    include_package_data=True,
    install_requires=install_requires,
    keywords='wind',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='wind',
    packages=find_packages(include=['wind', 'wind.*']),
    python_requires='>=3.4',
    setup_requires=setup_requires,
    test_suite='tests',
    url='https://github.com/D3-AI/wind',
    version='0.0.0-dev',
    zip_safe=False,
)
