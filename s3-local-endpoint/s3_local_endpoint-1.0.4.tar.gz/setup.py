# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


with open('README.rst') as readme:
    long_description = readme.read()


def recursive_requirements(requirement_file, libs, links, path=''):
    if not requirement_file.startswith(path):
        requirement_file = os.path.join(path, requirement_file)
    with open(requirement_file) as requirements:
        for requirement in requirements.readlines():
            if requirement.startswith('-r'):
                requirement_file = requirement.split()[1]
                if not path:
                    path = requirement_file.rsplit('/', 1)[0]
                recursive_requirements(requirement_file, libs, links,
                                       path=path)
            elif requirement.startswith('-f'):
                links.append(requirement.split()[1])
            else:
                libs.append(requirement)

libraries, dependency_links = [], []
recursive_requirements('requirements.txt', libraries, dependency_links)

setup(
    name='s3_local_endpoint',
    version='1.0.4',
    packages=find_packages(),
    install_requires=libraries,
    dependency_links=dependency_links,
    long_description=long_description,
    description='Library used as an S3 gateway abstraction over boto3 library.',
    author='di-dip-unistra',
    author_email='dnum-dip@unistra.fr',
    maintainer='di-dip-unistra',
    maintainer_email='dnum-dip@unistra.fr',
    url='https://git.unistra.fr/di/cesar/s3_local_endpoint.git',
    download_url='',
    license='GPLv3',
    keywords=['s3', 'Université de Strasbourg'],
    include_package_data=True,
)
