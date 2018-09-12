from setuptools import setup, find_packages


long_desc = """
fushare
===============
https://github.com/LowinLi/fushare
Installation
--------------
    pip install fushare

Upgrade
---------------
    pip install fushare --upgrade

"""




setup(
    name='fushare',
    version='1.1.5',
	install_requires = 
		['pandas>=0.23.1',
		'requests>=2.12.4',
		'bs4'],
    description='A utility for fundamentals data of China future',
	packages = ['fushare'],
	package_data={'': ['*.py','*.json']},
    long_description=long_desc,
    author='LowinLi',
    author_email='li783170560@126.cn',
    url = 'https://github.com/LowinLi/fushare',
    keywords='Fundmentals Future Data'
)

