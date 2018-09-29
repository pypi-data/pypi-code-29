# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['flake8_type_annotations']
install_requires = \
['flake8>=3.5,<4.0']

entry_points = \
{'flake8.extension': ['T8 = flake8_type_annotations:Checker']}

setup_kwargs = {
    'name': 'flake8-type-annotations',
    'version': '0.1.0',
    'description': 'Flake8 plugin to enforce consistent type annotation styles',
    'long_description': '# flake8-type-annotations\n\n[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/sobolevn/flake8-type-annotations.svg?branch=master)](https://travis-ci.org/sobolevn/flake8-type-annotations) [![Coverage](https://coveralls.io/repos/github/sobolevn/flake8-type-annotations/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/flake8-type-annotations?branch=master) [![Python Version](https://img.shields.io/pypi/pyversions/flake8-type-annotations.svg)](https://pypi.org/project/flake8-type-annotations/) [![PyPI version](https://badge.fury.io/py/flake8-type-annotations.svg)](https://pypi.org/project/flake8-type-annotations/)\n\nThis tool is used to validate type annotations syntax\nas it was [originally proposed](https://github.com/PyCQA/pycodestyle/issues/357)\nby [Guido van Rossum](https://github.com/gvanrossum).\n\n## Installation\n\n```bash\npip install flake8-type-annotations\n```\n\n## Code example\n\n```python\n# Consistency with this plugin:\ndef function(param=0, other: int = 0) -> int:\n    return param + other\n\n\n# Possible errors without this plugin:\ndef function(param=0, other: int=0)->int:\n    return param + other\n```\n\n## Error codes\n\n| Error code |                          Description                          |\n|:----------:|:-------------------------------------------------------------:|\n|    T800    | Missing spaces between parameter annotation and default value |\n|    T801    | Missing spaces in return type annotation                      |\n\n## License\n\nMIT.\n',
    'author': 'Nikita Sobolev',
    'author_email': 'mail@sobolevn.me',
    'url': 'https://github.com/sobolevn/flake8-type-annotations',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
