# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['nonrepeat']
setup_kwargs = {
    'name': 'nonrepeat',
    'version': '0.1.3',
    'description': 'Generate non-repeat filenames, ids and strings',
    'long_description': None,
    'author': 'Pacharapol Withayasakpunt',
    'author_email': 'patarapolw@gmail.com',
    'url': None,
    'py_modules': modules,
}


setup(**setup_kwargs)
