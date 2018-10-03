# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyhandsontable']

package_data = \
{'': ['*'], 'pyhandsontable': ['templates/*']}

install_requires = \
['jinja2>=2.10,<3.0', 'jupyter>=1.0,<2.0', 'notebook>=5.6,<6.0']

setup_kwargs = {
    'name': 'pyhandsontable',
    'version': '0.2.10',
    'description': 'Bring the power of Handsontable to Python and Jupyter Notebook',
    'long_description': '# pyhandsontable\n\n[![Build Status](https://travis-ci.org/patarapolw/pyhandsontable.svg?branch=master)](https://travis-ci.org/patarapolw/pyhandsontable)\n[![PyPI version shields.io](https://img.shields.io/pypi/v/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)\n[![PyPI license](https://img.shields.io/pypi/l/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)\n\nView a 2-D array, probably from [pyexcel](https://github.com/pyexcel/pyexcel) in Jupyter Notebook, and export to `*.html`.\n\n## Installation\n\n```commandline\npip install pyhandsontable\n```\n\n## Usage\n\n```python\n>>> from pyhandsontable import view_table\n>>> view_table(width=800, height=500, data=data_matrix, **kwargs)\nA Handsontable is shown in Jupyter Notebook.\n```\n\n## Acceptable kwargs\n\n- title: title of the HTML file\n- maxColWidth: maximum column width. (Default: 200)\n- renderers: the renderers to use in generating the columns (see below.)\n- autodelete: whether the temporary HTML file should be autodeleted. (Default: True)\n- filename: filename of the temporary HTML file (default: \'temp.handsontable.html\')\n- css: url of the Handsontable CSS\n- js: url of the Handsontable Javascript\n- config: add additional config as defined in https://docs.handsontable.com/pro/5.0.0/tutorial-introduction.html\n  - This will override the default config (per key basis) which are:\n  \n```javascript\n{\n  data: data\n  rowHeaders: true,\n  colHeaders: true,\n  dropdownMenu: true,\n  filters: true,\n  modifyColWidth: function(width, col){\n    if(width > maxColWidth) return maxColWidth;\n  }\n}\n```\n\n`renderers` example, if your data is a 2-D array:\n\n```python\n{\n    1: \'html\',\n    2: \'html\'\n}\n```\n\nor if your data is list of dict:\n\n```python\n{\n    "front": \'html\',\n    "back": \'html\'\n}\n```\n\n## Post-creation editing of the HTML\n\nYou might try `from bs4 import BeautifulSoup`:\n\n        renderers = {\n            1: \'markdownRenderer\',\n            2: \'markdownRenderer\'\n        }\n        config = {\n            \'colHeaders\': [\'id\'] + list(CardTuple._fields),\n            \'rowHeaders\': False\n        }\n\n        filename = \'temp.handsontable.html\'\n        try:\n            table = view_table(data=([[i] + list(record.to_formatted_tuple())\n                                      for i, record in self.find(keyword_regex, tags)]),\n                               width=width,\n                               height=height,\n                               renderers=renderers,\n                               config=config,\n                               filename=filename,\n                               autodelete=False)\n            with open(filename, \'r\') as f:\n                soup = BeautifulSoup(f.read(), \'html5lib\')\n\n            div = soup.new_tag(\'div\')\n\n            js_markdown = soup.new_tag(\'script\',\n                                       src=\'https://cdn.rawgit.com/showdownjs/showdown/1.8.6/dist/showdown.min.js\')\n            js_custom = soup.new_tag(\'script\')\n\n            with open(\'gflashcards/js/markdown-hot.js\') as f:\n                js_custom.append(f.read())\n\n            div.append(js_markdown)\n            div.append(js_custom)\n\n            script_tag = soup.find(\'script\', {\'id\': \'generateHandsontable\'})\n            soup.body.insert(soup.body.contents.index(script_tag), div)\n\n            with open(filename, \'w\') as f:\n                f.write(str(soup))\n\n            return table\n        finally:\n            Timer(5, os.unlink, args=[filename]).start()\n\n[Source](https://github.com/patarapolw/gflashcards/blob/master/gflashcards/app.py#L93)\n\n## Screenshots\n\n<img src="https://github.com/patarapolw/pyhandsontable/blob/master/screenshots/0.png" />\n\n## Related projects\n\n- https://github.com/patarapolw/gflashcards\n- https://github.com/patarapolw/jupyter-flashcards\n',
    'author': 'Pacharapol Withayasakpunt',
    'author_email': 'patarapolw@gmail.com',
    'url': 'https://github.com/patarapolw/pyhandsontable',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
