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
    'version': '0.4.2',
    'description': 'A Sphinx extension to assist in publishing scientific writing in either HTML or PDF.',
    'long_description': '# Sphinxience\n\nA Sphinx extension to assist in publishing scientific writing in either HTML or PDF. \n\nThis extension mainly consists of a number of roles and directives, so that you can use most LaTeX macros more easily than writing inline LaTeX in Sphinx. This extension will also change the LaTeX output, to conform to what is expected of scientific papers submitted to conferences/journals. By default, Sphinxience uses the `article` documentclass in LaTeX, but below there are instructions on how to fork Sphinxience so you can start to tweak every aspect of it.\n\nSphinxience is pronounced either like "Sphinx science" or rhyming with "experience". It\'s up to you.\n\n## How to use this\n\nThere are only a few options to set in the `conf.py` file in your Sphinx project, but the easiest way is probably to copy this template and to follow the instructions: https://github.com/bgeron/sphinxience-template .\n\nBecause Sphinxience modifies the internals of Sphinx\'s LaTeX rendering, it is unfortunately rather coupled to a specific version of Sphinx. Currently, that is Sphinx version 1.7. If you use Sphinxience via this template, then Poetry will make sure that you always use a compatible version of Sphinx.\n\n## How to fork and tweak this\n\nIf you writing substantive documents with this, you might well feel the need to further customize the available widgets and their LaTeX output. The best way is probably to\n\n1.  Fork this Sphinxience project locally,\n2.  Change the `sphinxience` line in the `pyproject.toml` for your Sphinx project:\n\n        sphinxience = {path = "/your/sphinxience/checkout"}\n\n3.  Use the local checkout in the virtualenv, by running\n\n        poetry install --develop=sphinxience\n\nIf you now run `make html` or `make latexpdf` again, then the local checkout of Sphinxience will be used.\n\nThis documentation will turn out useful: [Developing extensions for Sphinx](http://www.sphinx-doc.org/en/master/extdev/index.html).\n\nNote that if you change the intermediate doctrees that Sphinx produces, then it will not suffice to run `make html` or `make latexpdf` and you must additionally run `make clean`.\n\n## Status\n\n**Warning: I\'m still in the (slow) process of open sourcing this.**\n\nThis works:\n\n-   HTML output\n-   LaTeX output\n-   A `skip` directive that includes some vertical space, in both HTML and LaTeX:\n\n        .. skip:: big\n\n    (The `big` size corresponds to a LaTeX `\\bigskip`.)\n\nThis is still to do:\n\n-   Come up with a good way to write preambles for both the HTML and the LaTeX output. (In my PhD thesis, I have a rather hacky mechanism.)\n-   Some reasonable amount of documentation\n-   Open source my theorems/lemmas/etc directive, and the proof directive\n-   Open source my convenient role for `\\ref`\n-   Open source miscellaneous roles and directives\n\n\n## General note\n\nThe code here should work and be reasonable clean, but it could e.g. use a linter to catch unused imports. Patches are welcome! Also if you developed a new directive or role.\n\n',
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
