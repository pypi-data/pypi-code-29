from __future__ import print_function
import setuptools.command.install
import setuptools
import sys

class Install(setuptools.command.install.install):
    def run(self, *args, **kwargs):
        print()
        print('You probably meant to install multidocs!', file=sys.stderr)
        sys.exit(1)

setuptools.setup(
    name='multidoc',
    version='0.1',
    cmdclass={'install': Install},
)
