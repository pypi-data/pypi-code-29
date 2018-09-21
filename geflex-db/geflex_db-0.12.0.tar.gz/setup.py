from setuptools import setup

from geflex_db import __version__

setup(
    name='geflex_db',
    version=__version__,
    packages=['geflex_db'],
    url='https://github.com/geflex/geflex_db',
    license='Apache 2.0, see LICENSE file',
    author='geflex',
    author_email='geflikh.d.s@gmail.com',
    description='Simple tables and file objects for data storage and processing.'
)
