# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pillars',
 'pillars.engines',
 'pillars.middlewares',
 'pillars.sites',
 'pillars.transports']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=1.1,<2.0',
 'aiohttp>=3.3,<4.0',
 'aioredis>=1.1,<2.0',
 'aiosip',
 'async-timeout>=3.0,<4.0',
 'asyncpg>=0.17.0,<0.18.0',
 'attrs>=18.1,<19.0',
 'cchardet>=2.1,<3.0',
 'cerberus>=1.2,<2.0',
 'cython>=0.28.5,<0.29.0',
 'panoramisk',
 'pyyaml>=3.13,<4.0',
 'setproctitle>=1.1,<2.0',
 'ujson>=1.35,<2.0',
 'uvloop>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'pillars',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Pillars\n',
    'author': 'Allocloud',
    'author_email': 'allocloud@ovv.wtf',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
