#-*- coding:utf-8 -*-
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "txt_util",
    version = "0.0.1",
    author = "Meeyeong Im",
    author_email = "meeyeong1211@gmail.com",
    description = ("file_op;abs_path;cosine_sim;get_ngram;load_json;pos_tagging;time_printer."),
    license = "BSD",
    keywords = "some txt parsing util",
    
    packages=['txt_util'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

