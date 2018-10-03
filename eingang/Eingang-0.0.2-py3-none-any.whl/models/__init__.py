import glob
from os.path import dirname, basename, isfile

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

modules = glob.glob(dirname(__file__) + '/*.py')
modules = (basename(f)[:-3] for f in modules
           if isfile(f) and not f.endswith('__init__.py'))
for module in modules:
    exec('from .{} import *'.format(module))
