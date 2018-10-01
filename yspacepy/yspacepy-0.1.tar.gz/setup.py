
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='yspacepy',
      version='0.1',
      url='https://github.com/y-space/yspacepy',
      author='Nuno Carvalho',
      author_email='narcarvalho@gmail.com',
      description='http://y-space.pw companion package',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',
      packages=find_packages(),
      install_requires=['astropy'],
      zip_safe=False)

