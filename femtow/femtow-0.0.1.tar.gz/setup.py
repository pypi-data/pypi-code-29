# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['femtow', 'femtow.decorators']

package_data = \
{'': ['*'], 'femtow': ['templates/*']}

install_requires = \
['Routes>=2.4,<3.0',
 'backlash>=0.1.4,<0.2.0',
 'gunicorn>=19.9,<20.0',
 'mako>=1.0,<2.0',
 'venusian>=1.1,<2.0',
 'webob>=1.8,<2.0']

setup_kwargs = {
    'name': 'femtow',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Bruk Habtu',
    'author_email': 'bruk.habtu@gmail.com',
    'url': 'https://gitlab.com/brukhabtu/femtow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '3.7',
}


setup(**setup_kwargs)
