# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['carve']

package_data = \
{'': ['*']}

install_requires = \
['cytoolz>=0.9.0,<0.10.0', 'toolz>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'carve',
    'version': '0.2.1',
    'description': 'A minimalist Python library for manipulating nested data structures with ease and performance.',
    'long_description': '![](media/carve.png)\n\n# 🌲Carve\n\nA minimalist Python library for manipulating nested data structures with ease and performance.\n\nTake a look:\n\n```\n>>> from carve import treemap\n>>> obj = {"john": {"doe": [{"puma": "yes", "adidas": None}]}}\n>>> treemap(obj, remove_empty)\n{"john": {"doe": [{"puma": "yes"}]}}\n>>> treemap(obj, lambda k,v,p: ("PUMA", "puma") if k == "puma" else (k,v))\n{"john": {"doe": [{"PUMA": "puma", "adidas": None}]}}\n```\n\n## Quick Start\n\nInstall using pip/pipenv/etc. (we recommend [poetry](https://github.com/sdispater/poetry) for sane dependency management):\n\n```\n$ poetry add carve\n```\n\nTransform your dictionary using a `k,v,p` context for each operation:\n\n* k - key.\n* v - value.\n* p - path, in the form of a tuple: ("john", "doe") means the nested key "john.doe".\n\nAnd return a key-value tuple: `(key, value)`. You can:\n\n* Return a custom value to change both key and value `("foo", "bar")`\n* Just modify a key: `("foo", v)`\n* Just modify a value: `(k, "bar")`\n* Remove the current entry: `(None, None)`\n* Decide what to do based on your current path: `(None, None) if "secret" in p else (k,v)`\n\n## Builtins\n\nYou can use the following builtins for shortcut operations:\n\n```python\nfrom carve import treemap, mapkey, mapval, remove, on_key, remove_empty, flow\n\ntreemap(target, remove(lambda k, v, p: k == "adidas"))\ntreemap(target, mapval(lambda k, v, p: "X" if len(p) > 2 else v))\ntreemap(target, mapkey(lambda k, v, p: "X" + v if len(p) > 2 else k))\ntreemap(target, on_key("puma", lambda k, v, p: (k, "X")))\ntreemap(target, remove_empty)\n\n# multiple builtins, left-to-right with \'flow\'\nassert treemap(target, flow(scream, remove_empty))\n```\n\n\n### Thanks:\n\nTo all [Contributors](https://github.com/jondot/carve/graphs/contributors) - you make this happen, thanks!\n\n# Copyright\n\nCopyright (c) 2018 [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.',
    'author': 'Dotan Nahum',
    'author_email': 'jondotan@gmail.com',
    'url': 'https://github.com/jondot/carve',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
