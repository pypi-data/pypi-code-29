# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['diderypy',
 'diderypy.core',
 'diderypy.help',
 'diderypy.lib',
 'diderypy.models']

package_data = \
{'': ['*'], 'diderypy': ['flo/*']}

install_requires = \
['arrow>=0.12.1,<0.13.0',
 'click>=6.7,<7.0',
 'ioflo>=1.7,<2.0',
 'libnacl>=1.6,<2.0',
 'simplejson>=3.16,<4.0']

setup_kwargs = {
    'name': 'diderypy',
    'version': '0.0.1',
    'description': 'SDK for working with Didery servers',
    'long_description': None,
    'author': 'Nicholas Telfer',
    'author_email': 'ntelfer40@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.7',
}


setup(**setup_kwargs)
