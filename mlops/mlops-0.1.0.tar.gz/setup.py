# coding: utf-8

import sys
from setuptools import setup, find_packages

sys.path.append('./src')
import mlops as ml

REQUIRED_PACKAGES = [
  'tensorflow',
  'tensorflow-hub',
  'ruamel.yaml',
]

setup(
  name = 'mlops',
  version = ml.__version__,
  author='Arata Furukawa',
  author_email='info@ornew.net',
  url='https://github.com/ornew/mlops',
  install_requires = REQUIRED_PACKAGES,
  packages = find_packages('src'),
  package_dir = {'': 'src'},
  include_package_data = True,
  description = 'ML-ops',
  scripts = ['tools/tf-mlops'],
)
