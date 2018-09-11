# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['option']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'option',
    'version': '0.1.3',
    'description': 'Rust like Option type in Python',
    'long_description': '# Option\n',
    'author': 'Peijun Ma',
    'author_email': 'peijun.ma@protonmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
