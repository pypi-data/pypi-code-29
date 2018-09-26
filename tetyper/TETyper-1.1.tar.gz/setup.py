from setuptools import setup

setup(
	name='TETyper',
	version='1.1',
	author='Anna Sheppard',
	author_email='anna.sheppard@ndm.ox.ac.uk',
	url='https://github.com/aesheppard/TETyper',
	scripts=['TETyper.py'],
	install_requires=[
		'biopython',
		'pysam',
		'pyvcf'			
	]
)
