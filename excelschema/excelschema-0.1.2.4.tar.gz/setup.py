# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['excelschema']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.7,<3.0']

setup_kwargs = {
    'name': 'excelschema',
    'version': '0.1.2.4',
    'description': "Excel records' parser and schema viewing and validating tools.",
    'long_description': "# excelschema\n\nExcel records' parser and schema viewing and validating tools.\n\n## Installation\n\nMethod 1:\n\n```\n$ pip install excelschema\n```\n\nMethod 2:\n- Clone the project from GitHub\n- `poetry install`\n\n## Usage\n\nTo read an Excel file, you may also need to install [`pyexcel`](https://github.com/pyexcel/pyexcel) and [`pyexcel-xlsx`](https://github.com/pyexcel/pyexcel-xlsx) as well.\n\n```python\n>>> from excelschema import SchemaParser\n>>> import pyexcel\n>>> sp = SchemaParser(records=pyexcel.get_records(file_name='foo.xlsx', sheet_name='bar'))\n>>> sp.schema\n{\n    'record_id': <class 'int'>,\n    'modified': <class 'datetime.datetime'>,\n    'data': <class 'str'>\n}\n```\n\nValidating records and convert it to a usable one.\n\n```python\n>>> sp.ensure_one({'record_id': ' 12', 'data': 567})\n{'record_id', 12, 'data': '567'}\n```\n\nSetting constraints\n\n```python\n>>> from excelschema import Constraint\n>>> sp.update_schema({\n...     'user_id': Constraint(type_=int, unique=True, not_null=True)\n... })\n```\n\nIt is also possible to create an custom schema without an Excel\n\n```python\n>>> sp = SchemaParser(schema={\n...     'record_id': Constraint(type_=int, unique=True, not_null=True),\n...     'modified': datetime\n... })\n```\n\n## Bonus functions\n\nCleaning dirty Excel records\n\n```python\n>>> from excelschema import parse_record\n>>> parse_record({'foo': ' 1', 'bar': ' - ', 'baz': ' '})\n{'foo', 1}\n```\n\n\n## Related projects\n\n- https://github.com/patarapolw/tinydb-constraint\n",
    'author': 'patarapolw',
    'author_email': 'patarapolw@gmail.com',
    'url': 'https://github.com/patarapolw/excelschema',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
