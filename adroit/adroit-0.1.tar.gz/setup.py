# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['adroit']

package_data = \
{'': ['*'], 'adroit': ['docker/*']}

entry_points = \
{'console_scripts': ['adroit = adroit.cli:main']}

setup_kwargs = {
    'name': 'adroit',
    'version': '0.1',
    'description': 'Ansible Docker Role Testing',
    'long_description': '# `adroit` - Ansible Docker Role Testing\n\nHeavily opinionated tool for testing ansible roles using docker containers.\n\nThe tool will create a base image with the base role installed. This image\nwill be used for testing all roles.\n\nFor every role being tested, a docker container will be spun up, and an ad-hoc\nplaybook including only the one role will be ran twice: Once to verify that all\nthe tasks succeeded, then once again to ensure that the role is idempotent -\nthat is, that no new changes were introduced on the second run.\n',
    'author': 'Andreas Lutro',
    'author_email': 'anlutro@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
