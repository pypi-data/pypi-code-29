from setuptools import setup

version = '0.0.1'
name = 'mergepdf'
short_description = '`mergepdf` is a package for merge PDF files.'
long_description = """\
`mergepdf` is a package for merge PDF files.
::

   $ mergepdf -h
   usage: mergepdf [-h] [-i INPUT_DIR] [-o OUTPUT_FILE] [-k SORTED_KEY]
   
   Merge PDF files.
   
   optional arguments:
     -h, --help            show this help message and exit
     -i INPUT_DIR, --input-dir INPUT_DIR
     -o OUTPUT_FILE, --output-file OUTPUT_FILE
     -k SORTED_KEY, --sorted-key SORTED_KEY

Requirements
------------
* Python 3.6 later

Features
--------
* nothing

Setup
-----
::

   $ pip install mergepdf

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
    py_modules=['mergepdf'],
    keywords=['mergepdf',],
    author='Saito Tsutomu',
    author_email='tsutomu.saito@beproud.jp',
    url='https://pypi.python.org/pypi/mergepdf',
    license='PSFL',
    entry_points={
            'console_scripts':[
                'mergepdf = mergepdf:main',
            ],
        },
    install_requires=['PyPDF2'],
)
