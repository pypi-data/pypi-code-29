# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sphinxience']

package_data = \
{'': ['*'], 'sphinxience': ['static/*', 'templates/*']}

install_requires = \
['Sphinx>=1.7,<1.8', 'alabaster>=0.7,<0.8']

entry_points = \
{'sphinx.html_themes': ['sphinxience = sphinxience']}

setup_kwargs = {
    'name': 'sphinxience',
    'version': '0.3.1',
    'description': 'A Sphinx extension to assist in publishing scientific writing in either HTML or PDF.',
    'long_description': '# Sphinxience\n\nA Sphinx extension to assist in publishing scientific writing in either HTML or PDF. \n\nThis extension mainly consists of a number of roles and directives, so that you can use most LaTeX macros more easily than writing inline LaTeX in Sphinx. This extension will also monkeypatch your HTML theme and LaTeX settings, to make the LaTeX output conform to what is expected of scientific papers submitted to conferences/journals.\n\nSphinxience is pronounced either like "Sphinx science" or rhyming with "experience". It\'s up to you.\n\n## How to use this\n\nTODO copy an example project that I will make\n\n## How to fork this\n\nTODO\n\n## Status\n\n**Warning: I\'m still in the (slow) process of open sourcing this.**\n\nTODO There is some stuff in this project but it\'s still minimal. I\'m extracting it out from another project bit by bit. I\'ve only tested the HTML output; the LaTeX style is still pending.\n\n## Random stuff\n\nTODO generate documentation from source\n\nGeneral note about code quality: the code here should work and be reasonable clean, but it could e.g. use a linter to catch unused imports. Patches are welcome!\n\n',
    'author': 'Bram Geron',
    'author_email': 'bram@bram.xyz',
    'url': 'https://github.com/bgeron/sphinxience',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
