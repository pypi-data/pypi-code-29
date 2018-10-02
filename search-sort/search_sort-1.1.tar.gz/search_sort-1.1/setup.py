from setuptools import setup, find_packages

setup(name='search_sort',
      version='1.1',
	  url='https://github.com/Nikhil-Xavier-DS/Sort-Search-Algorithms',
      description='Search and Sort algorithms library',
      long_description=open('pip_search_sort.md').read(),
      author='Nikhil Xavier',
      author_email='nikhilxavier@yahoo.com',
      packages=find_packages(exclude=['tests']),
      zip_safe=False,
      keywords='search sort algorithms')