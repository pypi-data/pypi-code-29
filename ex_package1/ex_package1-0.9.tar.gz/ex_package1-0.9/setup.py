from setuptools import setup,find_packages
#from distutils.core import setup
setup(name='ex_package1',
      version='0.9',
      description='1st prog',
	  url='https://www.python.org/lavanya123/ex_packagev0.9',
      author='lavanya123',
      author_email='lavanyapavuluri@123.com',
      license='MIT',
	  #packages=['ex_package'],
	  packages=find_packages(),
      zip_safe=False)
     


