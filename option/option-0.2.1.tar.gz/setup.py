# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['option']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'option',
    'version': '0.2.1',
    'description': 'Rust like Option and Result types in Python',
    'long_description': "# Option\n[![Build Status](https://travis-ci.org/MaT1g3R/option.svg?branch=master)](https://travis-ci.org/MaT1g3R/option)\n[![codecov](https://codecov.io/gh/MaT1g3R/option/branch/master/graph/badge.svg)](https://codecov.io/gh/MaT1g3R/option)\n\nA [rust-like](https://doc.rust-lang.org/std/option/enum.Option.html) `Option` type in Python, slotted and fully typed.\n\nAn `Option` type represents an optional value, every `Option` is either `Some` and contains Some value, or `NONE`\n\nUsing an `Option` type forces you to deal with `None` values in your code and increase type safety.\n\n## Quick Start\n```Python\nfrom option import Result, Option, Ok, Err\nfrom requests import get\n\n\ndef call_api(url, params) -> Result[dict, int]:\n    result = get(url, params)\n    code = result.status_code\n    if code == 200:\n        return Ok(result.json())\n    return Err(code)\n\n\ndef calculate(url, params) -> Option[int]:\n    return call_api(url, params).ok().map(len)\n\n\ndict_len = calculate('https://example.com', {})\n```\n\n## Install\nOption can be installed from PyPi:\n```bash\npip install option\n```\n\n## Documentation\nThe documentation lives at https://mat1g3r.github.io/option/\n\n## License\nMIT\n",
    'author': 'Peijun Ma',
    'author_email': 'peijun.ma@protonmail.com',
    'url': 'https://mat1g3r.github.io/option/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
