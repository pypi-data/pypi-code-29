# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['deep_filter']
setup_kwargs = {
    'name': 'deep-filter',
    'version': '1.0.0',
    'description': 'Removes values from nested dicts and lists',
    'long_description': "# deep-filter\nA simple package that filters out values from dicts/lists, including all dicts/lists nested within it.\n\n# Usage\n```python\nfrom deep_filter import deep_filter\nx = {\n    'nope': 69,\n    'yep': [\n        69,\n        {'maybe': None},\n        99\n    ]\n}\ndef filter_func:\n    return value != 69\nresult = deep_filter(x, filter_func)\nprint(result)\n# {'yep': [{}, 99]}\n```\n\n#### deep_filter(dict_or_list, filter_func=default_filter_func)\n- **dict_or_list**: A dictionary or list\n- **filter_func**: An optional callback function. It will take a value as an argument, and return `True` if the value will be kept and `False` if not. If omitted, `None` values will be filtered out.\n\nReturns your dict or list, filtered.",
    'author': 'KH',
    'author_email': 'kasperkh.kh@gmail.com',
    'url': 'https://github.com/spectralkh/deep-filter',
    'py_modules': modules,
}


setup(**setup_kwargs)
