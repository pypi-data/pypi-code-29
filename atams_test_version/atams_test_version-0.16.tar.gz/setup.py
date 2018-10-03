from setuptools import setup,find_packages
from distutils.core import setup
import os,time
import sys
import pkg_resources
from distutils.dir_util import copy_tree
#datadir = os.path.join('static')


setup(name='atams_test_version',
      version='0.16',
      description='1st prog',
	  #scripts=['c:\\Users\\SIGPC4\\Desktop\\atams_test\\atams\\test1.py'],
	  
	  packages=find_packages(),
	  package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt','*.db', '*.xml', '*.special', '*.wsgi','*.so','*pyc'],},
	 data_files=("C:/Users/SIGPC4/Desktop/text/atams", ["static","templates"]),
	  
	  #recursive-include docs *,
      zip_safe = False)



