# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['scrmbl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'scrmbl',
    'version': '0.1.1',
    'description': 'Library for scrambled printing in terminal',
    'long_description': '# scrmbl <a href="https://gitter.im/scrmbl/Lobby"><img align="right" src="https://img.shields.io/badge/chat-on%20gitter-%234FB999.svg"></a><a href="https://coveralls.io/github/etienne-napoleone/scrmbl?branch=develop"><img align="right" src="https://coveralls.io/repos/github/etienne-napoleone/scrmbl/badge.svg?branch=develop"></a><a href="https://travis-ci.org/etienne-napoleone/scrmbl"><img align="right" src="https://travis-ci.org/etienne-napoleone/scrmbl.svg?branch=develop"></a>\n\n🕵️ Library for "scrambled" printing in terminal\n\n![demo gif](https://raw.githubusercontent.com/etienne-napoleone/scrmbl/develop/demo.gif)\n\n## Requirements\n\n- Tested on Python >= 3.5\n\n## Install\n\nUsing pip in a virtualenv.\n\n```bash\npip install scrmbl\n```\n\nUsing Poetry:\n\n```bash\npoetry add scrmbl\n```\n\nUsing pipenv:\n\n```bash\npipenv install scrmbl\n```\n\n## Usage\n\n```python\n>>> import scrmbl\n\n# refer to the gif to see the effect\n>>> scrmbl.echo(\'09:30pm, Washington, NSA HEADQUARTERS\')\n\'09:30pm, Washington, NSA HEADQUARTERS\'\n\n# handle multiline\n>>> scrmbl.echo(\'09:30pm, Washington\\nNSA HEADQUARTERS\')\n\'09:30pm, Washington\'\n\'NSA HEADQUARTERS\'\n\n# custom settings:\n# charset = List of characters to randomly iterate through\n# speed = Milliseconds to wait between each iteration\n# iterations = number of iterations before printing the final character\n>>> scrmbl.echo(\'NSA OFFICE\', charset=[\'N\', \'S\', \'A\'], speed=0.2, iterations=6)\n\'NSA OFFICE\'\n\n# premade charsets:\n# LETTERS_LOWER\n# LETTERS_UPPER\n# FIGURES\n# SPECIALS\n# LETTERS (LETTERS_LOWER + LETTERS_UPPER)\n# ALPHANUMERICS (LETTERS + FIGURES)\n# ALL (ALPHANUMERICS + SPECIALS)\n>>> scrmbl.echo(\'NSA OFFICE\', charset=scrmbl.charsets.LETTERS)\n\'NSA OFFICE\'\n```\n',
    'author': 'Etienne Napoleone',
    'author_email': 'etienne@tomochain.com',
    'url': 'https://github.com/etienne-napoleone/scrmbl',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
