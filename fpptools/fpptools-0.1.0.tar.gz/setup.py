# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fpptools']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0',
 'colorama>=0.3.9,<0.4.0',
 'configparser>=3.5,<4.0',
 'lxml>=4.2,<5.0',
 'pymysql>=0.9.2,<0.10.0',
 'pyodbc>=4.0,<5.0']

entry_points = \
{'console_scripts': ['fpptools = fpptools.fpptools:cli']}

setup_kwargs = {
    'name': 'fpptools',
    'version': '0.1.0',
    'description': '',
    'long_description': '# FppTools\n\nFppTools is a set of debugging tools geared towards the analysis and correction of str, blk and job files belonging to the implementation of the software [FP Pro](http://www.emmegisoft.com/en/product/fp-pro).',
    'author': 'andresperezcera',
    'author_email': 'andresperezcera@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
