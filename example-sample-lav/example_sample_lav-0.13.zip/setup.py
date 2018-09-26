#from setuptools import setup
from distutils.core import setup
setup(name='example_sample_lav',
      version='0.13',
      description='1st prog',
      url='https://www.python.org/lavanya123/example_sample_lav/',
      author='lavanya123',
      author_email='lavanyapavuluri@123.com',
      license='MIT',
      packages=['example_sample_lav'],
      zip_safe=False,
	  include_package_data=True)
import os
try:
  import requests
except ImportError:
  print "Trying to Install required module: requests\n"
  os.system('python -m pip install requests')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import requests	  


