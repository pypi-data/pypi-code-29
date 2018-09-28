#!/usr/bin/env python

"""
UNSIO : Universal Nbody Snapshot Input Output

"""

import numpy
import os
import sys
from setuptools import setup, Extension
from setuptools.command.build_py import build_py as _build_py


#  find out numpy include directory.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

if sys.version_info[:2] < (2, 7) or (3, 0) <= sys.version_info[:2] < (3, 4):
    raise RuntimeError("Python version 2.7 or >= 3.4 required.")

# detect python version (2 or 3)
pyversion = "3"
if sys.version_info[0] < 3:
    pyversion = ""


long_description = """\

UNSIO (*U*niversal *N*body *S*napshot *I*nput *O*utput) is an API which perform input/output operations in a generic way, and on different kind of nbody files format (nemo, Gadget binaries 1 and 2, Gadget hdf5, Ramses).

By using this API, a user could write only one analysis program which will work on all known files format supported by UNSIO.
It's not necessary anymore to know how is implemented a file format, UNSIO will do transparently and automatically all the hard work for you ! With UNSIO, you will spend less time to develop your analysis program.

UNSIO comes with an integrated sqlite3 database which can be used to retrieve automatically all your data among terabytes of hard disks.
"""


# trick to add SWIG generated module
# see https://stackoverflow.com/questions/12491328/python-distutils-not-include-the-swig-generated-module
# and especially : https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else/48942866#48942866
# and the fix for python2 https://stackoverflow.com/questions/1713038/super-fails-with-error-typeerror-argument-1-must-be-type-not-classobj-when/1713052#1713052

class build_py(_build_py, object):
    def run(self):
        self.run_command("build_ext")
        if pyversion == "":  # python2
            return super(build_py, self).run()
        else:                # python3
            return super().run()


#
# version management
#
MAJOR = '0'
MINOR = '9'
MICRO = '2rc1'
VERSION = '%s.%s.%s' % (MAJOR, MINOR, MICRO)

#
# write_version : write unsio version in py/unsio/version.py file
# it's imported from __init__.py as __version__


def write_version_py(filename='py/unsio/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM PYTHON-UNSIO SETUP.PY
#
version = '%(version)s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION})

    finally:
        a.close()

#
# setup_package :
#

def setup_package():
    # generate version
    write_version_py()

    # metada for setup
    metadata = dict(
        # name='python'+pyversion+'-unsio',
        name='python-unsio',
        version=VERSION,
        description='A python wrapper to unsio',
        long_description=long_description,
        author='Jean-Charles LAMBERT',
        author_email='jean-charles.lambert@lam.fr',
        url='https://projets.lam.fr/projects/unsio',
        license='CeCILL2.1 (https://opensource.org/licenses/CECILL-2.1)',
        classifiers=[
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Programming Language :: C",
            "Programming Language :: C++",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Topic :: Software Development"],
        platforms=["Linux", "Mac OS-X", "Unix"],
        python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
        package_dir={'': 'py'},  # all packages are under 'py' directory
        packages=['unsio', 'unsio/test'],
        # cmdclass = {'install':Build_ext_first},
        # cmdclass={'build': CustomBuild, 'install': CustomInstall},
        cmdclass={'build_py': build_py},
        py_modules=['unsio/py_unsio'],
        ext_modules=[
            Extension("unsio/_py_unsio",
                      sources=["py/unsio/py_unsio.i"],
                      swig_opts=['-c++', '-modern', '-Isrc',
                                 '-I./py/unsio', '-Iswig'],
                      include_dirs=[numpy_include, 'src'],
                      libraries=['unsio'],
                      library_dirs=[os.environ['HOME']+'/local/unsio/lib',
                                    '/usr/lib64', '/lib64'],
                      runtime_library_dirs=[
                          os.environ['HOME']+'/local/unsio/lib', '/usr/lib64', '/lib64']
                      )
        ],
        entry_points={
            "console_scripts": [
                "test_unsio_lib = unsio.test.ctestunsio:commandLine",
            ],
        },
        # install_requires=['numpy'],
        setup_requires=['numpy']
        #
    )
    setup(**metadata)


#
# main
#
if __name__ == '__main__':
    setup_package()
