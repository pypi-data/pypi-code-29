# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['diecast']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'diecast',
    'version': '0.3.1',
    'description': 'Dependency Injection framework for Python 3',
    'long_description': None,
    'author': 'Sean Johnson',
    'author_email': 'sean.johnson@maio.me',
    'url': 'https://glow.dev.maio.me/sjohnson/diecast',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
