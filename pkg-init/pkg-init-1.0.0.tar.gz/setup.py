# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

from setuptools import setup, find_packages


entry_points = {
    'console_scripts': [
        'package-init = pkg_init.core:main'
    ]
}


version = __import__('pkg_init').get_version()


setup(
    name="pkg-init",
    version=version,
    url='https://github.com/bluelief/pkg-init',
    author="bluelief",
    description="Initialize on a new package.",
    license="MIT",
    keywords="python, project",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese'
    ],
    project_urls={
        'Github': 'https://github.com/bluelief/pkg-init'
    }
)