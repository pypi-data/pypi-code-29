# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['scrmbl']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['scrmbl = scrmbl.cli:cli']}

setup_kwargs = {
    'name': 'scrmbl',
    'version': '1.0.0',
    'description': 'Library for scrambled printing in terminal',
    'long_description': '# scrmbl <a href="https://gitter.im/scrmbl/Lobby"><img align="right" src="https://img.shields.io/badge/chat-on%20gitter-%234FB999.svg"></a> <a href="https://coveralls.io/github/etienne-napoleone/scrmbl?branch=develop"><img align="right" src="https://coveralls.io/repos/github/etienne-napoleone/scrmbl/badge.svg?branch=develop"></a> <a href="https://travis-ci.org/etienne-napoleone/scrmbl"><img align="right" src="https://travis-ci.org/etienne-napoleone/scrmbl.svg?branch=develop"></a>\n\nLibrary and CLI for "scrambled" printing in terminal.\n\nHave you ever wanted your text to look like some corny action movie?\n\n![demo gif](https://raw.githubusercontent.com/etienne-napoleone/scrmbl/develop/demo.gif)\n\n## Requirements\n\n- Tested on Python >= 3.5\n\n## Install\n\n### CLI\n\n```\npip3 install --user scrmbl\n```\n\n### Library\n\nUsing pip in a virtualenv.\n\n```bash\npip install scrmbl\n```\n\nUsing Poetry:\n\n```bash\npoetry add scrmbl\n```\n\nUsing Pipenv:\n\n```bash\npipenv install scrmbl\n```\n\n## Usage\n\nRefer to the gif to see the effect\n\n### CLI\n\n```\nUsage: scrmbl [OPTIONS] [MESSAGE]\n\n  Scrmbl print the given message.\n\nOptions:\n  -s, --speed FLOAT         Time in seconds between prints. Default: 0.05\n  -i, --iterations INTEGER  Number of iterations per character. Default: 2\n  -c, --charset FILE        Set of chars to scramble.\n  --version                 Show the version and exit.\n  --help                    Show this message and exit.\n```\n\nCan also read from stdin.\n\n```bash\nls -lrtha | scrmbl\n```\n\n## Library\n\n```python\n>>> import scrmbl\n\n>>> scrmbl.echo(\'09:30pm, Washington, NSA HEADQUARTERS\')\n\'09:30pm, Washington, NSA HEADQUARTERS\'\n\n# handle multiline\n>>> scrmbl.echo(\'09:30pm, Washington\\nNSA HEADQUARTERS\')\n\'02:56am, New-York\'\n\'FBI HEADQUARTERS\'\n\n# custom settings:\n# charset = String of characters to scramble with\n# speed = Time in seconds between prints\n# iterations = number of iterations before printing the final character\n>>> scrmbl.echo(\'NSA OFFICE\', charset=\'ABCDefg/-\', speed=0.2, iterations=6)\n\'CIA OFFICE\'\n```\n\n## Thanks\n\nSpecial thanks for contributing:\n- [@podstava](https://github.com/podstava)\n- [@0jdxt](https://github.com/0jdxt)\n',
    'author': 'Etienne Napoleone',
    'author_email': 'etienne@tomochain.com',
    'url': 'https://github.com/etienne-napoleone/scrmbl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
