from setuptools import find_packages
from distutils.core import setup
setup(name='ex_package1',
      version='0.7',
      description='1st prog',
	  url='https://www.python.org/lavanya123/ex_package',
      author='lavanya123',
      author_email='lavanyapavuluri@123.com',
      license='MIT',
	  #packages=['ex_package'],
	  packages=find_packages(),
      zip_safe=False)
     


