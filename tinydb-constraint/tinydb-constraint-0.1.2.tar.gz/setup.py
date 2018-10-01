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
    'version': '0.1.2',
    'description': 'Apply constraints before inserting and updating TinyDB records.',
    'long_description': "# tinydb-constraint\n\n[![PyPI version shields.io](https://img.shields.io/pypi/v/tinydb-constraint.svg)](https://pypi.python.org/pypi/tinydb-constraint/)\n[![PyPI license](https://img.shields.io/pypi/l/tinydb-constraint.svg)](https://pypi.python.org/pypi/tinydb-constraint/)\n\nApply constraints before inserting and updating TinyDB records.\n\n## Installation\n\nMethod 1:\n\n```commandline\n$ pip install tinydb-constraint\n```\n\nMethod 2:\n\n- Clone the project from GitHub\n- [Get poetry](https://github.com/sdispater/poetry) and `poetry install tinydb-constraint --path PATH/TO/TINYDB/CONSTRAINT`\n\n## Usage\n\n```python\n>>> from tinydb import TinyDB\n>>> from tinydb_constraint import ConstraintTable\n>>> from datetime import datetime\n>>> db = TinyDB('db.json')\n>>> db.table_class = ConstraintTable\n>>> db.set_schema({\n...     'record_id': int,\n...     'modified': datetime\n... })\n>>> db.schema\n{\n    'record_id': Constraint(type_=int, unique=False, not_null=False),\n    'modified': Constraint(type_=datetime.datetime, unique=False, not_null=False)\n}\n```\n\nIf you want to enable TinyDB-constraint for all databases in a session, run:\n\n```python\n>>> from tinydb import TinyDB\n>>> from tinydb_constraint import ConstraintTable\n>>> TinyDB.table_class = ConstraintTable\n```\n\n## Note\n\nI haven't modified the serialization yet, so `datetime` type will actually produce `datetime.isoformat()`, and to set `datetime`, you have to pass a `dateutil.parser.parse()`-parsable string.\n\n## Advanced usage\n\nDatabase schema is also settable via `Constraint` object.\n\n```python\n>>> from tinydb_constraint import Constraint\n>>> db.set_schema({\n...     'user_id': Constraint(type_=int, unique=True, not_null=True)\n... })\n```\n\nIf you want to disable certain string sanitization features, like stripping spaces or checking if string can be converted to datetime, this can be done by setting environmental variables.\n\n```\nTINYDB_SANITIZE=0\nTINYDB_DATETIME=0\n```\n\n## Plan\n\n- Add ForeignKey constraints.\n\n## Related projects\n\n- [tinydb-viewer](https://github.com/patarapolw/tinydb-viewer) - View records generated from TinyDB and alike (e.g. list of dictionaries.)\n",
    'author': 'Pacharapol Withyasakpunt',
    'author_email': 'patarapolw@gmail.com',
    'url': 'https://github.com/patarapolw/tinydb-constraint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
