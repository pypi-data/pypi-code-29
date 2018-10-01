# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['colorboy']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.3.9,<0.4.0']

setup_kwargs = {
    'name': 'colorboy',
    'version': '1.0.0',
    'description': 'Easily add color to your strings',
    'long_description': "# colorboy\n\nEasily add color to your strings\n\n# Installation\npip install colorboy\n\n# Usage\n```python\nimport colorboy as cb\nprint(cb.cyan('Globgogabgalab'))\n\nfrom colorboy import cyan, red # import a specific colors, bg_colors and styles\nprint(cyan('Piz')+red('za'))\n\nfrom colorboy import * # import all colors, bg_colors and styles\nprint(green('Mayonnaise'))\n\nfrom colorboy.colors import * # import all colors\nprint(red('EDEN'))\nfrom colorboy.bg_colors import * # import all bg_colors\nprint(black_bg('Stephen'))\nfrom colorboy.styles import * # import all styles\nprint(bright('Crywolf'))\n```\n\n# Colors\nThese are all the color functions available through colorboy:\n```python\n# colors - available by importing colorboy or colorboy.colors\nblack\nred\ngreen\nyellow\nblue\nmagenta\ncyan\nwhite\n\n# bg_colors - available by importing colorboy or colorboy.bg_colors\nblack_bg\nred_bg\ngreen_bg\nyellow_bg\nblue_bg\nmagenta_bg\ncyan_bg\nwhite_bg\n\n# styles - available by importing colorboy or colorboy.styles\ndim\nbright\n\n```\n\n# Dev Instructions\n### Installation\n1. Install Python (Python 3.7 works, probably other versions too)\n2. Install [Poetry](https://poetry.eustace.io). Poetry is used to manage dependencies, the virtual environment and publishing to PyPI, so it's worth learning.\n3. Run `poetry install` to install Python package dependencies.\n\nFor VSCode to detect the Python virtual environment that Poetry creates, I ran `poetry config settings.virtualenvs.in-project true`. This command makes Poetry create your Python virtual environment inside the project folder. Now, you can set the `python.pythonPath` setting to `${workspaceFolder}/.venv/bin/python` in your workspace settings (or global if you want this to be the default).",
    'author': 'KH',
    'author_email': 'kasperkh.kh@gmail.com',
    'url': 'https://github.com/spectralkh/colorboy-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
