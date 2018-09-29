from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import subprocess
from setuptools.command.install import install

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='kiwipiepy',

    version='0.5.1',

    description='Kiwi for Python',
    long_description=long_description,

    url='https://github.com/bab2min/kiwi',

    author='bab2min',
    author_email='bab2min@gmail.com',

    license='LGPL v3 License',

    classifiers=[
        'Development Status :: 3 - Alpha',

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Linguistic",

        "License :: OSI Approved :: LGPL v3 License",

        'Programming Language :: Python :: 3',
        'Programming Language :: C++'
    ],

    keywords='korean morphological analysis',

    packages = ['kiwipiepy'],
    include_package_data=True,
)
