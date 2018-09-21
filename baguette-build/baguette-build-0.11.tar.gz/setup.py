#-*- coding:utf-8 -*-
"""
Setup for baguette-build package.
"""
from setuptools import find_packages, setup

setup(
    name='baguette-build',
    version='0.11',
    url='https://wwww.baguette.io',
    author_email='pydavid@baguette.io',
    packages=find_packages(),
    platforms=[
        'Linux/UNIX',
        'MacOS',
        'Windows'
    ],
    install_requires=[
        'boto3==1.6.21',
        'docker==3.1.4',
        'GitPython==2.1.0',
        'kaptan==0.5.8',
        'baguette-messaging[postgres]',
        'baguette-utils',
        'python-slugify==1.2.4',
    ],
    extras_require={
        'testing': [
            'baguette-messaging[testing]',
            'mock==2.0.0',
            'pytest==3.0.7',
            'pytest-cov==2.3.0',
            'pylint==1.6.1',
        ],
        'doc': [
            'Sphinx==1.4.4',
        ],
    },
    package_data={
        'cuisson': ['templates/deploy_post.tmpl', 'templates/deploy_put.tmpl'],
        'cuisson.tests': ['farine.ini', 'pytest.ini'],
    },
)
