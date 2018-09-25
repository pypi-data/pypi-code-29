# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['wemake_python_styleguide',
 'wemake_python_styleguide.errors',
 'wemake_python_styleguide.logics',
 'wemake_python_styleguide.options',
 'wemake_python_styleguide.visitors',
 'wemake_python_styleguide.visitors.ast',
 'wemake_python_styleguide.visitors.ast.complexity',
 'wemake_python_styleguide.visitors.ast.general',
 'wemake_python_styleguide.visitors.filenames',
 'wemake_python_styleguide.visitors.presets',
 'wemake_python_styleguide.visitors.tokenize']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=18.2,<19.0',
 'flake8-bandit>=1.0,<2.0',
 'flake8-bugbear>=18.2,<19.0',
 'flake8-builtins>=1.4,<2.0',
 'flake8-coding>=1.3,<2.0',
 'flake8-commas>=2.0,<3.0',
 'flake8-comprehensions>=1.4,<2.0',
 'flake8-debugger>=3.1,<4.0',
 'flake8-docstrings>=1.3,<2.0',
 'flake8-eradicate>=0.1,<0.2',
 'flake8-isort>=2.5,<3.0',
 'flake8-pep3101>=1.2,<2.0',
 'flake8-quotes>=1.0,<2.0',
 'flake8-string-format>=0.2,<0.3',
 'flake8-super-call>=1.0,<2.0',
 'flake8>=3.5,<4.0',
 'pep8-naming>=0.7,<0.8',
 'pycodestyle==2.3.1']

entry_points = \
{'flake8.extension': ['Z = wemake_python_styleguide.checker:Checker']}

setup_kwargs = {
    'name': 'wemake-python-styleguide',
    'version': '0.0.15',
    'description': 'The most opinionated linter ever, used by wemake.services',
    'long_description': "# wemake-python-styleguide\n\n[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)\n[![Build Status](https://travis-ci.org/wemake-services/wemake-python-styleguide.svg?branch=master)](https://travis-ci.org/wemake-services/wemake-python-styleguide)\n[![Coverage](https://coveralls.io/repos/github/wemake-services/wemake-python-styleguide/badge.svg?branch=master)](https://coveralls.io/github/wemake-services/wemake-python-styleguide?branch=master)\n[![PyPI version](https://badge.fury.io/py/wemake-python-styleguide.svg)](https://badge.fury.io/py/wemake-python-styleguide)\n[![Documentation Status](https://readthedocs.org/projects/wemake-python-styleguide/badge/?version=latest)](https://wemake-python-styleguide.readthedocs.io/en/latest/?badge=latest)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/wemake-python-styleguide/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n\nWelcome to the most opinionated linter ever.\n\nThe main goal of this tool is to make our `python` code\nconsistent and to fight the code complexity.\n\n`wemake-python-styleguide` is actually `flake8` plugin\nwith some other plugins as dependencies.\n\n```text\nThe Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!\n```\n\n\n## Installation\n\n```bash\npip install wemake-python-styleguide\n```\n\n\n## Project status\n\nWe are almost ready for our first public release.\nUntil, use it on your own risk.\n\n\n## What we are not\n\nWe are here not to:\n\n1. Assume or check types, use `mypy` instead\n2. Reformat code, since we believe that developers should do that\n3. Check for `SyntaxError`s or exceptions, write tests instead\n4. Suite everyone, this is *our* linter\n\n\n## Contributing\n\nSee [CONTRIBUTING.md](https://github.com/wemake-services/wemake-python-styleguide/blob/master/CONTRIBUTING.md) file if you want to contribute.\nYou can also check which [issues need some help](https://github.com/wemake-services/wemake-python-styleguide/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) right now.\n\n\n## License\n\nMIT. See [LICENSE](https://github.com/wemake-services/wemake-python-styleguide/blob/master/LICENSE) for more details.\n",
    'author': 'Nikita Sobolev',
    'author_email': 'mail@sobolevn.me',
    'url': 'https://github.com/wemake-services/wemake-python-styleguide',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
