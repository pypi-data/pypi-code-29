# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['imagedb']

package_data = \
{'': ['*'], 'imagedb': ['static/*', 'templates/*']}

install_requires = \
['flask>=1.0,<2.0',
 'nonrepeat>=0.1.1,<0.2.0',
 'pillow>=5.2,<6.0',
 'python-slugify>=1.2,<2.0',
 'sqlalchemy>=1.2,<2.0']

setup_kwargs = {
    'name': 'imagedb',
    'version': '0.1.2',
    'description': 'Store images, especially from Clipboard, in database',
    'long_description': None,
    'author': 'patarapolw',
    'author_email': 'patarapolw@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
