# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['imagedb']

package_data = \
{'': ['*'], 'imagedb': ['static/*', 'templates/*']}

install_requires = \
['click>=6.7,<7.0',
 'flask>=1.0,<2.0',
 'imagehash>=4.0,<5.0',
 'jupyter>=1.0,<2.0',
 'nonrepeat>=0.1.1,<0.2.0',
 'notebook>=5.6,<6.0',
 'pillow>=5.2,<6.0',
 'python-slugify>=1.2,<2.0',
 'send2trash>=1.5,<2.0',
 'sqlalchemy>=1.2,<2.0']

setup_kwargs = {
    'name': 'imagedb',
    'version': '0.1.6.3',
    'description': 'Store images, especially from Clipboard, in a database, and spin an image server (for usage in Jupyter Notebook).',
    'long_description': '# ImageDB\n\nStore images, especially from Clipboard, in a database, and spin an image server (for usage in Jupyter Notebook).\n\n## Installation\n\n```commandline\n$ pip install imagedb\n```\n\nOr\n\n1. Clone the project from GitHub\n2. `poetry add imagedb --path path/to/imagedb/folder`\n\n## Usage\n\n### Run an image server\n\nIn a Python script (outside Jupyter Notebook).\n\n```python\nfrom imagedb import ImageDB\nImageDB(\'images.db\').runserver()\n# Then, go to `http://localhost:8000` in your browser to register an image (from the clipboard).\n```\n\n### Get images from the image server\n\nIn Jupyter Notebook\n\n```pydocstring\n>>> from imagedb import ImageDB\n>>> idb = ImageDB(\'images.db\')\n>>> idb.last()\n# The latest image in the server will be shown.  `idb.last(5)` is also supported.\n>>> from IPython.display import display\n>>> for image in idb.search(tags=\'bar\'):\n...     display(image)\n# All images corresponding to the tag \'bar\' will be shown.\n```\n\n## Screenshots\n\n<img src="https://raw.githubusercontent.com/patarapolw/ImageDB/master/screenshots/jupyter1.png" />\n<img src="https://raw.githubusercontent.com/patarapolw/ImageDB/master/screenshots/jupyter2.png" />\n<img src="https://raw.githubusercontent.com/patarapolw/ImageDB/master/screenshots/browser1.png" />\n<img src="https://raw.githubusercontent.com/patarapolw/ImageDB/master/screenshots/browser2.png" />\n',
    'author': 'Pacharapol Withayasakpunt',
    'author_email': 'patarapolw@gmail.com',
    'url': 'https://github.com/patarapolw/ImageDB',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
