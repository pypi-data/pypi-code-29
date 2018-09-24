# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fact_sphere_cli']

package_data = \
{'': ['*']}

install_requires = \
['click-default-group>=1.2,<2.0', 'click>=6.0,<7.0', 'fact-sphere>=1.0,<2.0']

extras_require = \
{'dev': ['flake8>=3.5,<4.0',
         'flake8-builtins>=1.0,<2.0',
         'flake8-import-order>=0.18,<0.19',
         'flake8-import-order-tbm>=1.0.0,<2.0.0',
         'poetry>=0.9,<0.10'],
 'lint': ['flake8>=3.5,<4.0',
          'flake8-builtins>=1.0,<2.0',
          'flake8-import-order>=0.18,<0.19',
          'flake8-import-order-tbm>=1.0.0,<2.0.0']}

entry_points = \
{'console_scripts': ['fact-sphere = fact_sphere_cli.cli:fact_sphere_cli']}

setup_kwargs = {
    'name': 'fact-sphere-cli',
    'version': '1.0.0',
    'description': 'A CLI for Portal 2 Fact Sphere facts.',
    'long_description': '# fact-sphere-cli\n\n[fact-sphere-cli](https://github.com/thebigmunch/fact-sphere-cli) is a CLI for Portal 2 Fact Sphere facts using the\n[fact-sphere](https://github.com/thebigmunch/fact-sphere) library.\n\n\n## Installation\n\n``pip install fact-sphere-cli``\n\n\n## Usage\n\n```\nUsage: fact-sphere [OPTIONS] COMMAND\n\n  A CLI for Portal 2 Fact Sphere facts.\n\nOptions:\n  -V, --version  Show the version and exit.\n  -h, --help     Show this message and exit.\n\nCommands:\n  text*  Get the text for a random fact.\n  audio  Get the filepath or file content for a random fact.\n  fact   Get the text, filepath, and type for a random fact.\n```\n\nA plain ``fact-sphere`` call defaults to running the ``text`` command.\n\nThe only option is for the ``audio`` command. Use ``--read`` option\nto output the binary file content of the audio for piping.\n\n\n## Appreciation\n\nShowing appreciation is always welcome.\n\n#### Thank\n\n[![Say Thanks](https://img.shields.io/badge/thank-thebigmunch-blue.svg?style=flat-square)](https://saythanks.io/to/thebigmunch)\n\nGet your own thanks inbox at [SayThanks.io](https://saythanks.io/).\n\n#### Contribute\n\n[Contribute](https://github.com/thebigmunch/fact-sphere-cli/blob/master/CONTRIBUTING.md) by submitting bug reports, feature requests, or code.\n\n#### Help Others/Stay Informed\n\n[Discourse forum](https://forum.thebigmunch.me/)\n\n#### Referrals/Donations\n\n[![Coinbase](https://img.shields.io/badge/Coinbase-referral-orange.svg?style=flat-square)](https://www.coinbase.com/join/52502f01e0fdd4d3ef000253) [![Digital Ocean](https://img.shields.io/badge/Digital_Ocean-referral-orange.svg?style=flat-square)](https://m.do.co/c/3823208a0597) [![Namecheap](https://img.shields.io/badge/Namecheap-referral-orange.svg?style=flat-square)](https://www.namecheap.com/?aff=67208) [![PayPal](https://img.shields.io/badge/PayPal-donate-brightgreen.svg?style=flat-square)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=DHDVLSYW8V8N4&lc=US&item_name=thebigmunch&currency_code=USD)\n\n**BTC:** ``1BMLCFPcX8YHE1He2t3aBrsNDGr1pKhfFa``  \n**ETH:** ``0x8E3f8d8eAedeA61Bf34A998A2104954FE508D5d0``  \n**LTC:** ``LgsQU1YaY4a4s7m9efjn6m35XhVEpW1xoP``\n',
    'author': 'thebigmunch',
    'author_email': 'mail@thebigmunch.me',
    'url': 'https://github.com/thebigmunch/fact-sphere-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
