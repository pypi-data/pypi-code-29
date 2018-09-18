#!/usr/bin/env python
import os
import sys
from shutil import rmtree

from setuptools import setup, Command

NAME = 'tipico'
DESCRIPTION = 'useless client of a simulated device with PLICO'
URL = 'https://github.com/lbusoni/tipico'
EMAIL = 'lorenzo.busoni@inaf.it'
AUTHOR = 'Lorenzo Busoni'
LICENSE= 'MIT'
KEYWORDS= 'plico, laboratory, instrumentation control'

here = os.path.abspath(os.path.dirname(__file__))
# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)



class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(name=NAME,
      description=DESCRIPTION,
      version=about['__version__'],
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      long_description=open('README.md').read(),
      url='',
      author_email=EMAIL,
      author=AUTHOR,
      license=LICENSE,
      keywords=KEYWORDS,
      packages=['tipico',
                'tipico.calibration',
                'tipico.client',
                'tipico.gui',
                'tipico.types',
                'tipico.utils',
                ],
      entry_points={
          'gui_scripts': [
              'tipico_basic_pyqt5_gui=tipico.gui.basic_pyqt5:main',
              'tipico_basic_pyside2_gui=tipico.gui.basic_pyside2:main',
              'tipico_basic_qt_gui=tipico.gui.basic_qt:main',
          ],
      },
      package_data={
          'tipico': ['conf/tipico.conf'],
      },
      install_requires=["plico>=0.15",
                        "numpy",
                        "psutil",
                        "configparser",
                        "six",
                        "appdirs",
                        "pyfits",
                        "futures",
                        'pyside2',
                        "Qt.py",
                        "pathlib2; python_version < '3'"
                        ],
      include_package_data=True,
      cmdclass={'upload': UploadCommand, },
      test_suite='test',
      )
