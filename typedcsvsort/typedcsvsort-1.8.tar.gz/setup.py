import os
from distutils.core import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='typedcsvsort', 
    version='1.8',
    packages=['csvsort'],
    package_dir={'csvsort' : '.'}, 
    author='Jayme McKiney',
    author_email='jayme.mckiney@gmail.com',
    description='Sort large CSV files on disk rather than in memory',
    long_description=read('README.rst'),
    url='https://jmckiney@bitbucket.org/jmckiney/csvsort',
    license='lgpl',
)
