# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aiohttp_session_ws']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.4,<4.0', 'aiohttp_session>=2.5,<3.0']

setup_kwargs = {
    'name': 'aiohttp-session-ws',
    'version': '1.1.0',
    'description': '',
    'long_description': None,
    'author': 'Devin Fee',
    'author_email': 'devin@devinfee.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
