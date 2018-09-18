from setuptools import *

with open('requirements.txt') as f_required:
    required = f_required.read().splitlines()
with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
	name='MongoRandomizer',
	version='0.3.9',
	py_modules=['MongoRandomizer'],
	packages=find_packages(),
	install_requires=required,
	long_description=long_description,
    long_description_content_type="text/markdown",
	author="graboskyc",
	author_email="chris@grabosky.net",
	description="A small and basic package to create randomized MongoDB documents and trivial load.",
    url="https://github.com/graboskyc/MongoDataRandomizer",
	entry_points='''
		[console_scripts]
		MongoRandomizer=MongoRandomizer:cli
	''',
)