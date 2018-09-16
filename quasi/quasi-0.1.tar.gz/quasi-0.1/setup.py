# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.org') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = [
    'sanic',
    'requests_cache',
]

setup(
    name='quasi',
    version='0.1',
    description='Simple request wrapper',
    long_description=readme,
    author='Oliver Marks',
    author_email='oly@digitaloctave.com',
    url='https://gitlab.com/olymk2/quasi',
    license=license,
    package_data={'quasi': ['README.org', 'LICENSE']},
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    setup_requires=[],
    tests_require=['pytest']
)
