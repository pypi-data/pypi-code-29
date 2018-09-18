from setuptools import setup, find_packages
with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
	name='MongoRandomizer',
	version='0.3.7',
	py_modules=['MongoRandomizer'],
	packages=find_packages(),
	install_requires=['requests',],
	author="graboskyc",
	author_email="chris@grabosky.net",
	description="A small and basic package to create randomized MongoDB documents and trivial load.",
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/graboskyc/MongoDataRandomizer",
	entry_points='''
		[console_scripts]
		MongoRandomizer=MongoRandomizer:cli
	''',
)