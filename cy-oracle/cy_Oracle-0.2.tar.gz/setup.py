
from setuptools import setup

def readme():
	with open('README.rst','r') as f:
		return f.read()

setup(name='cy_Oracle',
      version='0.2',
      description='Extension to cx_Oracle to handle Oracle object types',
      long_description=readme(),
      author='Nuuk Zweiundvierzig',
      author_email='nuuk42@yahoo.com',
      license='MIT',
      packages=['cy_Oracle'],
      install_requires=['cx-Oracle'],
      include_package_data=True,
      zip_safe=False)
