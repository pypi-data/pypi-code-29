from setuptools import setup

import subprocess

try:  # Try to create an rst long_description from README.md
    args = "pandoc", "--to", "rst", "README.md"
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    print("README.md conversion to reStructuredText failed. Error:\n",
          error, "Setting long_description to None.")
    long_description = None

setup(
    name='uifunc',
    version='0.1.6',
    packages=['uifunc'],
    url='https://github.com/Palpatineli/uifunc',
    download_url='https://github.com/Palpatineli/uifunc/archive/0.1.5.tar.gz',
    license='GPLv3',
    author='Keji Li',
    author_email='mail@keji.li',
    extras_require={'wx': ['wx'], 'qt': ['PyQt5']},
    description='convenience functions for opening and saving files/folders',
    long_description=long_description,
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 3']
)
