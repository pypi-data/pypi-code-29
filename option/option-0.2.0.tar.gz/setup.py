# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['option']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'option',
    'version': '0.2.0',
    'description': 'Rust like Option type in Python',
    'long_description': '# Option\n[![Build Status](https://travis-ci.org/MaT1g3R/option.svg?branch=master)](https://travis-ci.org/MaT1g3R/option)\n[![codecov](https://codecov.io/gh/MaT1g3R/option/branch/master/graph/badge.svg)](https://codecov.io/gh/MaT1g3R/option)\n\nA [rust-like](https://doc.rust-lang.org/std/option/enum.Option.html) `Option` type in Python, slotted and fully typed.\n\nAn `Option` type represents an optional value, every `Option` is either `Some` and contains Some value, or `NONE`\n\nUsing an `Option` type forces you to deal with `None` values in your code and increase type safety.\n\n## Quick Start\n```Python\nfrom option import Some, NONE, Option\nfrom requests import get\n\ndef call_api(url, params) -> Option[dict]:\n    result = get(url, params)\n    if result.status_code == 200:\n        return Some(result.json())\n    return NONE\n\n# Instead of checking for None, the NONE case is always dealt with.\ndict_len = call_api(url, params).map(len)\n```\n\n## Install\nOption can be installed from PyPi:\n```bash\npip install option\n```\n\n## Documentation\nThe documentation lives at https://mat1g3r.github.io/option/\n\n## License\nMIT\n',
    'author': 'Peijun Ma',
    'author_email': 'peijun.ma@protonmail.com',
    'url': 'https://mat1g3r.github.io/option/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
