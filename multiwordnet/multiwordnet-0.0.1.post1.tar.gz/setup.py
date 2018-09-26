from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='multiwordnet',
      version='0.0.1.post1',
      description='A helper library for accessing and manipulating WordNets in the MultiWordNet',
      long_description=long_description,
      url='',
      author='William Michael Short',
      author_email='w.short@exeter.ac.uk',
      license='Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)',
      packages=['multiwordnet'],
      zip_safe=False)