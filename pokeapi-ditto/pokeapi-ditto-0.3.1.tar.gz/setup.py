# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pokeapi_ditto', 'pokeapi_ditto.commands']

package_data = \
{'': ['*']}

install_requires = \
['flask-cors>=3.0,<4.0',
 'flask>=1.0,<2.0',
 'genson>=1.0,<2.0',
 'gevent>=1.3,<2.0',
 'requests>=2.19,<3.0',
 'tqdm>=4.25,<5.0']

entry_points = \
{'console_scripts': ['ditto = pokeapi_ditto.main:main']}

setup_kwargs = {
    'name': 'pokeapi-ditto',
    'version': '0.3.1',
    'description': "Ditto is a server that serves a static copy of PokeAPI's data.",
    'long_description': "# Ditto\n\n[https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pokémon)](https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pok%C3%A9mon))\n\nThis repository contains:\n\n - Ditto script:\n    - `ditto clone`: a script to crawl an instance of PokeAPI and download all objects\n    - `ditto analyze`: a script to generate a JSON schema of the above data\n    - `ditto transform`: a script to apply a new base url to data in `data/api` \n    - `ditto serve`: a script to serve the data in the same form as PokeAPI\n       - with full support for dynamic pagination using GET args `offset` and `limit`\n - Static data:\n    - [data/api](data/api): a static copy of the JSON data generated with the above script\n    - [data/schema](data/schema): a static copy of the PokeAPI schema generated from the above data\n    - [updater](updater): a bot that runs in docker and can update the data stored in this repo\n\n## Docker\n\nThis project is on Docker Hub. If you just want to serve a PokeApi clone, you\njust have to run one command.\n\n - Replace `8080` with the port of your choice\n - Replace `http://localhost:8080` with the base url of your choice\n\n``` bash\ndocker run -p 8080:80 -e DITTO_BASE_URL=http://localhost:8080 sargunv/pokeapi-ditto:latest\n```\n\n## Usage\n\nIf you'd rather use the data for something else, you can generate a\ncopy with the base url of your choice applied. This assumes\n[Poetry](https://poetry.eustace.io/) is installed and in your PATH. \n\n``` bash\ngit clone https://github.com/PokeAPI/ditto.git\ncd ditto\npoetry install\npoetry run ditto transform --base-url http://localhost:8080\n```\n\nFor other ditto functionality, run `poetry run ditto --help` \n\nIf you're on Windows, you'll have to adapt the commands above to your platform.\nThe general idea is the same.\n\n## Advanced\n\nYou can manually update the data if necessary. See [the updater bot](updater). You can run the bot in docker, or read and adapt its update script yourself. \n",
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
