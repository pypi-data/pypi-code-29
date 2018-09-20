# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


with open('version.cache', 'r') as f:
    version = f.read()


setup(
    name="beamism",
    version=version,
    packages=find_packages(),
    description='welcome to beamism',
    long_description=readme,
    url='https://github.com/kyu999/beamism',
    author='kyu999',
    author_email='kyukokkyou999@gmail.com',
    maintainer='kyu999',
    maintainer_email='kyukokkyou999@gmail.com',
    platforms='Linux, Darwin',
    zip_safe=False,
    include_package_data=True,
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ]
)
