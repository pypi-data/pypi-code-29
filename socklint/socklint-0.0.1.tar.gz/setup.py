from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='socklint',
    version=__version__,
    description='API objects used by Sock Puppet',
    long_description=long_description,
    url='https://github.com/JesseTG/socklint',
    download_url='https://github.com/JesseTG/socklint/tarball/' + __version__,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Jesse Talavera-Greenberg',
    author_email='jessetalavera@aol.com'
)
