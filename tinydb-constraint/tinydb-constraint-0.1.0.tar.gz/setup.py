# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['tinydb_constraint']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.7,<3.0', 'tinydb>=3.11,<4.0']

setup_kwargs = {
    'name': 'tinydb-constraint',
    'version': '0.1.0',
    'description': 'Apply constraints before inserting and updating TinyDB records.',
    'long_description': "# tinydb-constraint\n\nApply constraints before inserting and updating TinyDB records.\n\n## Installation\n\nMethod 1:\n\n```commandline\n$ pip install tinydb-constraint\n```\n\nMethod 2:\n\n- Clone the project from GitHub\n- [Get poetry](https://github.com/sdispater/poetry) and `poetry install tinydb-constraint --path PATH/TO/TINYDB/CONSTRAINT`\n\n## Usage\n\n```python\n>>> from tinydb import TinyDB\n>>> from tinydb_constraint import ConstraintTable\n>>> from datetime import datetime\n>>> db = TinyDB('db.json')\n>>> db.table_class = ConstraintTable\n>>> db.schema = {\n...     'record_id': int,\n...     'modified': datetime\n... }\n```\n\nIf you want to enable TinyDB-constraint for all databases in a session, run:\n\n```python\n>>> from tinydb import TinyDB\n>>> from tinydb_constraint import ConstraintTable\n>>> TinyDB.table_class = ConstraintTable\n```\n\n## Note\n\nI haven't modified the serialization yet, so `datetime` type will actually produce `datetime.isoformat()`, and to set `datetime`, you have to pass a `dateutil.parser.parse()`-parsable string.\n\n## Related projects\n\n- [tinydb-viewer](https://github.com/patarapolw/tinydb-viewer) - View records generated from TinyDB and alike (e.g. list of dictionaries.)\n",
    'author': 'Pacharapol Withyasakpunt',
    'author_email': 'patarapolw@gmail.com',
    'url': 'https://github.com/patarapolw/tinydb-constraint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
