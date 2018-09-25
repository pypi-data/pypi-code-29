#!/usr/bin/env python3

from setuptools import find_packages, setup

if __name__ == "__main__":
	setup(
		name = "prolice",
		version = "0.2.0",
		author = "Stefan Mavrodiev",
		author_email = "stefan.mavrodiev@gmail.com",
		maintainer = "Stefan Mavrodiev",
		maintainer_email = "stefan.mavrodiev@gmail.com",
		description = "Command line interface for flashing iCE40HX1K-EVB",
		long_description = open("README.md").read() + open("CHANGELOG.md").read(),
		long_description_content_type="text/markdown",
		url = "https://gitlab.com/stefan.mavrodiev/prolice",
		install_requires = [
			"pyftdi >= 0.20",
			"pyspiflash >= 0.5",
			"halo"
		],
		entry_points = {
			"console_scripts" : [
				"prolice = prolice.prolice:main"
			]
		},
		packages=find_packages(),
		python_requires = ">=3.5",
		classifiers = [
			"Development Status :: 4 - Beta",
			"Environment :: Console",
			"Intended Audience :: Developers",
			"Intended Audience :: Education",
			"Intended Audience :: End Users/Desktop",
			"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
			"Operating System :: POSIX :: Linux",
			"Programming Language :: Python",
			"Programming Language :: Python :: 3 :: Only"
		]
	)
