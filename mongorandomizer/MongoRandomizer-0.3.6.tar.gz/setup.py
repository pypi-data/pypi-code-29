from setuptools import setup, find_packages

setup(
	name='MongoRandomizer',
	version='0.3.6',
	py_modules=['MongoRandomizer'],
	packages=find_packages(),
	install_requires=['requests',],
	author="graboskyc",
	author_email="chris@grabosky.net",
	entry_points='''
		[console_scripts]
		MongoRandomizer=MongoRandomizer:cli
	''',
)