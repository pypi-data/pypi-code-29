# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['flake8_eradicate']
install_requires = \
['attrs>=18.2.0,<19.0.0', 'eradicate>=0.2.1,<0.3.0', 'flake8>=3.5,<4.0']

entry_points = \
{'flake8.extension': ['E8 = flake8_eradicate:Checker']}

setup_kwargs = {
    'name': 'flake8-eradicate',
    'version': '0.1.1',
    'description': 'Flake8 plugin to find commented out code',
    'long_description': '# flake8-eradicate\n\n`flake8` plugin to find commented out (or so called "dead") code.\n\nThis is quite important for the project in a long run.\nThis tool is based on [`eradicate`](https://github.com/myint/eradicate) project.\n\n[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/sobolevn/flake8-eradicate.svg?branch=master)](https://travis-ci.org/sobolevn/flake8-eradicate) [![Coverage](https://coveralls.io/repos/github/sobolevn/flake8-eradicate/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/flake8-eradicate?branch=master) [![Python Version](https://img.shields.io/pypi/pyversions/flake8-eradicate.svg)](https://pypi.org/project/flake8-eradicate/) [![PyPI version](https://badge.fury.io/py/flake8-eradicate.svg)](https://badge.fury.io/py/flake8-eradicate)\n\n## Installation\n\n```bash\npip install flake8-eradicate\n```\n\n## Usage\n\nRun your `flake8` checker [as usual](http://flake8.pycqa.org/en/latest/user/invocation.html).\nCommented code should raise an error.\n\nWe prefer not to raise a warning than to raise a false positive.\nSo, we ignore `--aggressive` option from `eradicate`.\n\n## Error codes\n\n| Error code |        Description       |\n|:----------:|:------------------------:|\n|    E800    | Found commented out code |\n\n## Output example\n\n```terminal\n» flake8 tests/fixtures/incorrect.py\ntests/fixtures/incorrect.py:1:1: E800: Found commented out code:\n--- before/tests/fixtures/incorrect.py\n+++ after/tests/fixtures/incorrect.py\n@@ -1,16 +1,10 @@\n\n class Some(object):\n-    # property_name = 1\n     other_property = 2\n\n\n-# def function_name():\n-#     return None\n\n\n-# class CommentedClass(object):\n #     def __init__(self) -> None:\n-#         self.property = None\n\n #     def __str__(self) -> str:\n-#         return self.__class__.__name__\n```\n\n## License\n\nMIT.\n',
    'author': 'Nikita Sobolev',
    'author_email': 'mail@sobolevn.me',
    'url': 'https://github.com/sobolevn/flake8-eradicate',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
