# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name='knowhere',
 version='1.0.0',
 packages=['knowhere'],
 license = 'MIT',
 description = 'An in memory cache with efficient expiration',
 author = 'Sankalp Jonna',
 author_email = 'sankalpjonna@gmail.com',
 keywords = ['cache','memory','in memory','expiration','ttl'],
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/sankalpjonn/knowhere",
 include_package_data=True,
 install_requires=['timeloop', 'xxhash'],
)
