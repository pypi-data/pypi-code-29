# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['cranial']

package_data = \
{'': ['*'],
 'cranial': ['examples/*',
             'models/*',
             'models/tests/*',
             'models/tests/data/*',
             'tests/*']}

install_requires = \
['cranial-datastore>=0.2.0,<0.3.0',
 'cranial-messaging>=0.2.0,<0.3.0',
 'docopt>=0.6.2,<0.7.0',
 'pathos>=0.2.2,<0.3.0']

setup_kwargs = {
    'name': 'cranial-modeling',
    'version': '0.2.0',
    'description': 'Standard model interface, where "model" means any stateless or stateful transformation of data & scripts for deploying Models as services.',
    'long_description': None,
    'author': 'Mikhail Erekhinsky',
    'author_email': 'merekhinsky@tribuneinteractive.com',
    'url': 'https://github.com/tribune/cranial-modeling',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
