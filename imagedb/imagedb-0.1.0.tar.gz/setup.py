# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['imagedb']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=5.2,<6.0', 'sqlalchemy>=1.2,<2.0']

setup_kwargs = {
    'name': 'imagedb',
    'version': '0.1.0',
    'description': 'Store images, especially from Clipboard, in a single file',
    'long_description': None,
    'author': 'patarapolw',
    'author_email': 'patarapolw@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
