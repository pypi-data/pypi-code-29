"""_____________________________________________________________________

:PROJECT: LARA

*labpy setup *

:details: labpy setup file for installation.
         - For installation, run:
           run pip3 install .
           or  python3 setup.py install

:file:    setup.py
:authors: mark doerr (mark.doerr@uni-greifswald.de)

:date: 20180918         
:date: 20180918

.. note:: -
.. todo:: - 
________________________________________________________________________
"""
__version__ = "0.0.1"

import os
import sys

from setuptools import setup, find_packages
#~ from distutils.sysconfig import get_python_lib

pkg_name = 'labpy'

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

install_requires = [] 
data_files = []
    
setup(name=pkg_name,
    version=__version__,
    description='labpy - python a labor (automation) environment ',
    long_description=read('README.rst'),
    author='mark doerr',
    author_email='mark.doerr@uni-greifswald.de',
    keywords='lab automation, Qt5, PySide2, laboratory, instruments, experiments, database, evaluation, visualisation, SiLA2, robots',
    url='https://gitlab.com/LARAsuite/pylab',
    license='MIT',
    packages=find_packages(), #['pylab'],
    #~ package_dir={'pylab':'pylab'},
    install_requires = install_requires,
    test_suite='',
    classifiers=[  'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Utilities'],
    include_package_data=True,
    data_files=data_files,
)
