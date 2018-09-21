import setuptools
with open("README.md", "r") as fh:
	long_description = fh.read()
setuptools.setup(
	name="pypi_install",
	version="0.0.4",
	author="Osama Arshad Dar",
	author_email="14beeodar@seecs.edu.pk",
	description="Uploading code to PyPi made easy",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/daroodar/Pypi-Install",
	packages=setuptools.find_packages(),
	classifiers=[
	"Programming Language :: Python :: 2",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
	],
)