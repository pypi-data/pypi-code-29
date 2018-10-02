""" Core Utils """

import re
import importlib

from ruamel.yaml import YAML

def import_module(name):
  """ wrapper importlib.import_module """
  return importlib.import_module(name=name)

def load_yaml(path):
  #TODO: handle error
  return YAML().load_all(open(path))

_chain_case = re.compile(r'([a-z0-9])([A-Z])')
def to_chain_case(name):
  return _chain_case.sub(r'\1-\2', name).lower()

def to_pascal_case(name):
  return name.title().replace('-','')