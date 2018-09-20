"""
NLopt
=====

NLOpt is a free/open-source library for nonlinear optimization, providing a common interface for a number of different free optimization routines available online as well as original implementations of various other algorithms.

The code is exactly as found in https://github.com/stevengj/nlopt/releases. NLOpt is compiled without Guile, Octave and Matlab.

This package is just a distribution of NLopt. The person marked as the author of this package is just the author of the PyPI package, not of NLopt. The post-release version corresponds to the version of the PyPI package itself (the actual NLOpt does not use that version segment).
"""

import os
import sys
import glob
import shutil

import platform
import subprocess

import setuptools
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext


class CustomExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CustomBuild(build_ext):
    def run(self):
        if platform.system() == "Windows":
            raise RuntimeError("this thing has never ever been built on Windows...")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        try:
            import numpy
        except:
            raise Exception("numpy is not present. Build will fail")

        build_cmd = ['make','install']

        config_cmd = [os.path.join(ext.sourcedir, 'configure'),
                      '--prefix={}'.format(os.path.abspath(self.build_temp)),
                      '--libdir={}'.format(extdir),
                      '--enable-shared',
                      # these try to install in their directory if found, must be optional
                      '--without-guile',
                      '--without-octave',
                      '--without-matlab'
        ]
        if self.debug:
            config_cmd.append('--enable-debug')
        print(' '.join(config_cmd))
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        print('extdir: {}'.format(extdir))
        print('build_temp: {}'.format(self.build_temp))

        subprocess.check_call(config_cmd, cwd=self.build_temp, env=os.environ)
        subprocess.check_call(build_cmd, cwd=self.build_temp, env=os.environ)
        # nlopt things are copied in 'lib/python%s/site-packages/ and it is not set by an option, AFAIK, so I copy them
        # the following cannot be right!
        for f in glob.glob(os.path.join(self.build_temp, 'lib/python%s/site-packages/*'%(sys.version[:3]))):
            if os.path.isfile(f):
                shutil.copy(f, extdir)
        for f in glob.glob(os.path.join(self.build_temp, 'lib64/python%s/site-packages/*'%(sys.version[:3]))):
            if os.path.isfile(f):
                shutil.copy(f, extdir)

        if platform.system() == 'Darwin':
            for l in glob.glob(os.path.join(extdir,'_nlopt*.so')):
                for l2 in glob.glob(os.path.join(extdir,'lib*.dylib')):
                    l3 = l2.replace(extdir, '@loader_path')
                    cmd = ['install_name_tool', '-change', l2, l3, l]
                    subprocess.call(cmd)
setup(
    name='nlopt',
    version='2.4.2.post2',
    description='NLopt. A free/open-source library for nonlinear optimization',

    # parameters from now on are optional
    long_description=__doc__,

    url='https://nlopt.readthedocs.io',
    author='Javier G. Gonzalez',
    author_email='javierggt@yahoo.com',

    install_requires=['numpy'],

    ext_modules=[CustomExtension('nlopt')],
    cmdclass={'build_ext':CustomBuild,},
    zip_safe=False,
    packages=find_packages(),

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    # Note that this is a string of words separated by whitespace, not a list.
    # keywords='',

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # project_urls={
    #    'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #    'Funding': 'https://donate.pypi.org',
    #    'Say Thanks!': 'http://saythanks.io/to/example',
    #    'Source': 'https://github.com/pypa/sampleproject/',
    #},
)
