from __future__ import print_function
from distutils.command.install import install
import setuptools
import sys

class Install(install):
    def run(self):
        print('You probably meant to install multidocs!', file=sys.stderr)
        sys.exit(1)

setuptools.setup(
    name='multidoc',
    cmdclass={'install': Install},
)
