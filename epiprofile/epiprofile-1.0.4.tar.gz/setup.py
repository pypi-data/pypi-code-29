import sys, os, platform, glob
from distutils.core import setup
from setuptools import *

"""
Setup script for epidaurus
"""

if sys.version_info[0] != 2 or sys.version_info[1] < 7:
	print >> sys.stderr, "ERROR: Epiprofile (epidaurus) requires Python 2.7"
	sys.exit()
	

def main():
	setup(  name = "epiprofile",
			version = "1.0.4",
			py_modules = [ 'psyco_full' ],
			packages = find_packages( 'lib' ),
			package_dir = { '': 'lib' },
			package_data = { '': ['*.ps'] },
			scripts = glob.glob( "bin/*.py"),
			ext_modules = [],
			test_suite = 'nose.collector',
			setup_requires = ['nose>=0.10.4','cython>=0.12'],
			author = "Liguo Wang",
			author_email ="wangliguo78@gmail.com",
			platforms = ['Linux','MacOS'],
			requires = [],
			install_requires = ['bx-python','numpy','scipy'], 
			description = "Epidaurus is a program to visualize the epigenomic landscape of genomic regions of interest (TF bindings, TSS, etc).",
			url = "http://epidaurus.sourceforge.net/",
			zip_safe = False,
			dependency_links = ['https://github.com/bxlab/bx-python', 'https://pypi.org/project/numpy/', 'https://github.com/scipy/scipy'],
			classifiers=[
				'Development Status :: 5 - Production/Stable',
				'Environment :: Console',
				'Intended Audience :: Science/Research',
				'License :: OSI Approved :: MIT License',
				'Operating System :: MacOS :: MacOS X',
				'Operating System :: POSIX',
				'Programming Language :: Python',
				'Topic :: Scientific/Engineering :: Bio-Informatics',
			],
			
			keywords='epigenomic, visualize, bigwig',
             )


if __name__ == "__main__":
	main()
