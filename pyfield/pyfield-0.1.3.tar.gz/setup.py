# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['pyfield', 'pyfield.field', 'pyfield.validator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfield',
    'version': '0.1.3',
    'description': 'Collection of field for your form',
    'long_description': "=======\npyfield\n=======\n\n.. image:: https://travis-ci.org/Ublimjo/pyfield.svg?branch=master\n    :target: https://travis-ci.org/Ublimjo/pyfield\n\nCollection of field for your form **not** *only web form*\n\n\nDescription\n===========\n\n**pyfield** is a collection of field with battery included.\n\nThis project is under developmment, please read\n`CONTIBUTING.rst <https://github.com/Ublimjo/pyfield/blob/master/CONTRIBUTING.rst>`_\n\n\nExample\n=======\n\n.. code-block:: python\n\n >>> from pyfield import Text\n >>>\n >>> def main():\n >>>     username = Text('Username')\n >>>     username(input(username.prompt_input()))\n >>>     print(f'Your name is {username.get}')\n >>>\n >>> main()\n  Username: Bob\n Your name is Bob\n\nIt's very simple but pyfield comes with a lot of features\n\n - Default value\n - Transformator\n - Validator\n\nRead the docs if you want to know more about these features or create your own\nTransformator and validator\n\n\n",
    'author': 'Ublim',
    'author_email': 'ublimjo@gmail.com',
    'url': 'https://github.com/Ublimjo/pyfield',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
