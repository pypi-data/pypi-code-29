import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hddtempnc",
    version="1.3.0",
    author="Viharm",
    author_email="viharm@malviya.net",
    description="Tool to acquire hard disk drive temperature from the network interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viharm/HDDtempNC",
    packages=setuptools.find_packages(),
    keywords='python hddtemp netcat terminal hdd',
    project_urls={
      'Bug Reports': 'https://github.com/viharm/HDDtempNC/issues',
      'Source': 'https://github.com/viharm/HDDtempNC',
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: System :: Hardware",
        "Topic :: System :: Monitoring",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
)