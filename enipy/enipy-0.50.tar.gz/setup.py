from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
  
import numpy
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
ext = Extension("enipy.lxcTools", ["enipy/lxcTools.pyx"], 
    include_dirs = [numpy.get_include()])

setuptools.setup(
    name="enipy",
    version="0.50",
    author="Micheal Stock",
    author_email="mstock@earthnetworks.com",
    description="Tool for analyzing Lightning Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
)	
