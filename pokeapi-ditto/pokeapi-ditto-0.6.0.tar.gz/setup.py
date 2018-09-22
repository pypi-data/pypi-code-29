# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pokeapi_ditto', 'pokeapi_ditto.commands']

package_data = \
{'': ['*']}

install_requires = \
['genson>=1.0,<2.0',
 'odictliteral>=1.0,<2.0',
 'requests>=2.19,<3.0',
 'tqdm>=4.26,<5.0',
 'yarl>=1.2,<2.0']

entry_points = \
{'console_scripts': ['ditto = pokeapi_ditto.main:main']}

setup_kwargs = {
    'name': 'pokeapi-ditto',
    'version': '0.6.0',
    'description': "Ditto is a server that serves a static copy of PokeAPI's data.",
    'long_description': '# Ditto\n\n[https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pokémon)](https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pok%C3%A9mon))\n\nThis repository contains:\n\n - `ditto clone`: a script to crawl an instance of PokeAPI and download all data\n - `ditto analyze`: a script to generate a JSON schema of the above data\n - `ditto transform`: a script to apply a new base url to the above data and schema\n\n## Usage\n\n```\npip install pokeapi-ditto\nditto --help\n```\n',
    'author': 'Sargun Vohra',
    'author_email': 'sargun.vohra@gmail.com',
    'url': 'https://github.com/PokeAPI/ditto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
