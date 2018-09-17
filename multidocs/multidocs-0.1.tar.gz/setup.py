# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['multidocs', 'multidocs.content', 'multidocs.sources', 'multidocs.web.auth']

package_data = \
{'': ['*'], 'multidocs': ['templates/*', 'web/*', 'web/static/*']}

install_requires = \
['bleach>=2.1,<3.0',
 'commonmarkextensions>=0.8,<0.9',
 'flask-oauthlib>=0.9,<0.10',
 'flask>=1.0,<2.0',
 'jinja2>=2.8,<3.0',
 'python-slugify>=0.12,<0.13',
 'pyyaml>=3.12,<4.0',
 'whoosh>=2.7,<3.0']

entry_points = \
{'console_scripts': ['multidocs = multidocs.cli:main']}

setup_kwargs = {
    'name': 'multidocs',
    'version': '0.1',
    'description': 'Generate documentation from multiple sources.',
    'long_description': '# multidocs\n\nGenerate a searchable HTML website with documentation from multiple git repositories containing Markdown files.\n\n## Installing\n\n```\npipsi install multidocs\nmultidocs -c /path/to/multidocs.yml generate\nmultidocs -c /path/to/multidocs.yml serve\n```\n\n## Developing\n\n```bash\npython3 -m venv .venv\nsource .venv/bin/activate\npip install -U pip setuptools poetry\npoetry develop\nmultidocs --help\n```\n',
    'author': 'Andreas Lutro',
    'author_email': 'anlutro@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
