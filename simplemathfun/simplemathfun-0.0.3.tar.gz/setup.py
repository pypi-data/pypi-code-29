import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "simplemathfun",
	version = "0.0.3",
	author = "sOBrien",
	author_email = "sobrien@elliottmgmt.com",
	description = "A small math package for tests",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/sOBrien/simplemathfun",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
