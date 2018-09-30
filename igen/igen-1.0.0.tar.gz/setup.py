from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name = 'igen',
	version = '1.0.0',
	author="Tuan Truong",
	author_email="tuan188@gmail.com",
	description="Code Generator Tools for iOS",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/tuan188/MGiOSTools",
	packages = ['igen', 'igen_templates'],
	entry_points = {
		'console_scripts': [
			'igen = igen.__main__:main'
		]
	},
	classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	include_package_data = True
	)