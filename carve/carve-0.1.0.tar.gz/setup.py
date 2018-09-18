# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['carve']

package_data = \
{'': ['*']}

install_requires = \
['cytoolz>=0.9.0,<0.10.0', 'toolz>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'carve',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dotan Nahum',
    'author_email': 'jondotan@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
