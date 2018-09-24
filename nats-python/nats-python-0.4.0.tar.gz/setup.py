# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pynats']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'nats-python',
    'version': '0.4.0',
    'description': 'Python client for NATS messaging system',
    'long_description': '# nats-python [![Build Status](https://travis-ci.org/Gr1N/nats-python.svg?branch=master)](https://travis-ci.org/Gr1N/nats-python) [![codecov](https://codecov.io/gh/Gr1N/nats-python/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/nats-python) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\nPython client for NATS messaging system.\n\nThis project is a replacement for abandoned [pynats](https://github.com/mcuadros/pynats). `nats-python` supports only Python 3.6+ and fully covered with typings.\n\nGo to the [asyncio-nats](https://github.com/nats-io/asyncio-nats) project, if you\'re looking for `asyncio` implementation.\n\n## Installation\n\n    $ pip install nats-python\n\n## Usage\n\n    from pynats import NATSClient\n\n    with NATSClient() as client:\n        client.publish("test-subject", payload=b"test-payload")\n\n## Contributing\n\nTo work on the `nats-python` codebase, you\'ll want to clone the project locally and install the required dependencies via [poetry](https://poetry.eustace.io):\n\n    $ git clone git@github.com:Gr1N/nats-python.git\n    $ poetry install\n\nTo run tests and linters use command below:\n\n    $ poetry run tox\n\nIf you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:\n\n    $ poetry run tox -e py37-tests\n\n## License\n\n`nats-python` is licensed under the MIT license. See the license file for details.\n',
    'author': 'Nikita Grishko',
    'author_email': 'gr1n@protonmail.com',
    'url': 'https://github.com/Gr1N/nats-python',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
