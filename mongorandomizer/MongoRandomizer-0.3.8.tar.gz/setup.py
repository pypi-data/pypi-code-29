from setuptools import setup, find_packages

setup(
	name='MongoRandomizer',
	version='0.3.8',
	py_modules=['MongoRandomizer'],
	packages=find_packages(),
	install_requires=['requests',],
	author="graboskyc",
	author_email="chris@grabosky.net",
	description="A small and basic package to create randomized MongoDB documents and trivial load.",
    url="https://github.com/graboskyc/MongoDataRandomizer",
	entry_points='''
		[console_scripts]
		MongoRandomizer=MongoRandomizer:cli
	''',
)