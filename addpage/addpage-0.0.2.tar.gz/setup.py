from setuptools import setup

version = '0.0.2'
name = 'addpage'
short_description = '`addpage` is a package for adding page number to PDF file.'
long_description = """\
`addpage` is a package for adding page number to PDF file.
::

   $ addpage -h
   usage: addpage [-h] [-o OUTFILE] [-n FONT_NAME] [-z FONT_SIZE] [-s START]
                  [-k SKIP] [-x MARGIN_X] [-y MARGIN_Y]
                  [-a {center,left,right}] [-f FORMAT]
                  infile
   
   Add page number to PDF file.
   
   positional arguments:
     infile                input PDF file
   
   optional arguments:
     -h, --help            show this help message and exit
     -o OUTFILE, --outfile OUTFILE
     -n FONT_NAME, --font-name FONT_NAME
     -z FONT_SIZE, --font-size FONT_SIZE
     -s START, --start START
     -k SKIP, --skip SKIP
     -x MARGIN_X, --margin-x MARGIN_X
     -y MARGIN_Y, --margin-y MARGIN_Y
     -a {center,left,right}, --alignment {center,left,right}
     -f FORMAT, --format FORMAT


Requirements
------------
* Python 3.6 later

Features
--------
* nothing

Setup
-----
::

   $ pip install addpage

History
-------
0.0.1 (2018-9-23)
~~~~~~~~~~~~~~~~~~
* first release

"""

classifiers = [
   "Development Status :: 1 - Planning",
   "License :: OSI Approved :: Python Software Foundation License",
   "Programming Language :: Python",
   "Topic :: Software Development",
   "Topic :: Scientific/Engineering",
]

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    py_modules=['addpage'],
    keywords=['addpage',],
    author='Saito Tsutomu',
    author_email='tsutomu.saito@beproud.jp',
    url='https://pypi.python.org/pypi/addpage',
    license='PSFL',
    entry_points={
            'console_scripts':[
                'addpage = addpage:main',
            ],
        },
    install_requires=['PyPDF2', 'reportlab', 'pdfformfiller'],
)
