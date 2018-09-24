from distutils.core import setup
from pkgutil import walk_packages

import shutterstock


def find_packages(path, prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name


setup(
  name='shutterstock',
  packages=list(find_packages(shutterstock.__path__, shutterstock.__name__)),
  version='0.1.2',
  description='Python Shutterstock API Client',
  author='Matt Roberts',
  author_email='contact@maleero.com',
  url='https://github.com/malero/python-shutterstock-api',
  download_url='https://github.com/malero/python-shutterstock-api/archive/v0.1.2.tar.gz',
  keywords=['shutterstock', ],
  classifiers=[],
)
