from inspect import cleandoc

from setuptools import setup


_version = {}
exec(open('hoursofoperation/_version.py').read(), _version)


setup(
  name = 'hoursofoperation',
  packages = ['hoursofoperation', 'hoursofoperation.test'],
  version = _version['__version__'],
  description = 'Utilities for loading and doing calculations with a partner\'s hours of operations configration.',
  author = 'Ashley Fisher',
  author_email = 'fish.ash@gmail.com',
  url = 'https://github.com/Brightmd/hoursofoperation',
  keywords = ['hours'],
  classifiers = [],
  scripts = [],
  install_requires=cleandoc('''
    codado>=0.6,<0.7
    python-dateutil==2.4.0
    pytz==2015.4
    ''').split()
)
