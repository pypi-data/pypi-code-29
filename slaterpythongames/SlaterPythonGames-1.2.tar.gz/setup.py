import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='SlaterPythonGames',
    version="1.2",
    description="An updated version of rygames, a collection of games written in Python",
    author="Ryan J. Slater",
    author_email="ryan.j.slater.2@gmail.com",
    url="https://github.com/rjslater2000/SlaterPythonGames",
    packages=setuptools.find_packages(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords=['games', 'battleship', 'python'],
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    install_requires=['pygame', 'numpy', 'matplotlib', 'names', 'requests'],
    )
