import setuptools


with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="numdata",
	version="2.0.0",
	author="Vinay Phadnis",
	author_email="abc@xyz.com",
	description="A simple package calculating values for a simgle number and created in my Udemy course",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="",
	keywords='package numbers calculations',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2",
		"Operating System :: OS Independent"
	],
	)

