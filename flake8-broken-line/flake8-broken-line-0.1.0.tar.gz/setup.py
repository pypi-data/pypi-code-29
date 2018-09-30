# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['flake8_broken_line']
install_requires = \
['flake8>=3.5,<4.0']

entry_points = \
{'flake8.extension': ['N4 = flake8_broken_line:check_line_breaks']}

setup_kwargs = {
    'name': 'flake8-broken-line',
    'version': '0.1.0',
    'description': 'Flake8 plugin to forbid backslashes for line breaks',
    'long_description': '# flake8-broken-line\n\n[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/sobolevn/flake8-broken-line.svg?branch=master)](https://travis-ci.org/sobolevn/flake8-broken-line) [![Coverage](https://coveralls.io/repos/github/sobolevn/flake8-broken-line/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/flake8-broken-line?branch=master) [![Python Version](https://img.shields.io/pypi/pyversions/flake8-broken-line.svg)](https://pypi.org/project/flake8-broken-line/) [![PyPI version](https://badge.fury.io/py/flake8-broken-line.svg)](https://pypi.org/project/flake8-broken-line/)\n\nDo not break the line! 🚨\n\n## Installation\n\n```bash\npip install flake8-broken-line\n```\n\n## Code example\n\nThings we check with this plugin:\n\n```python\n# String line breaks, use `()` or `"""` instead:\n\nsome_string = \'first line\\\nsecond line\'\n\n# Use a single line, `()`, or new variables instead:\n\nif 1 == 1 and \\\n    2 == 2:\n    print(\'Do not do that!\')\n\n# Do not reimplement chaining:\nsome_object \\\n  .call_method() \\\n  .call_other() \\\n  .finalize()\n\n```\n\n## Error codes\n\n| Error code |                   Description                 |\n|:----------:|:---------------------------------------------:|\n|    N400    | Found backslash that is used for line braking |\n\n## License\n\nMIT.\n',
    'author': 'Nikita Sobolev',
    'author_email': 'mail@sobolevn.me',
    'url': 'https://github.com/sobolevn/flake8-broken-line',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
