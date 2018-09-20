import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='batchbook-python',
      version='0.1.0',
      description='Batchbook API written in python',
      long_description=read('README.md'),
      author='Lelia Rubiano',
      author_email='lrubiano5@gmail.com',
      url='https://github.com/GearPlug/batchbook-python',
      packages=['batchbook'],
      install_requires=[
          'requests',
      ],
      keywords='batchbook',
      zip_safe=False,
      license='GPL',
     )