import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IFTTTtoDomoticzUsingPushover",
    version="0.9.3",
    author="Joe Houghton",
    author_email="github_joe_Houghton@outlook.com",
    description="Accepts Pushover commands and forwards them to Domoticz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joe-houghton/IFTTTtoDomoticzUsingPushover",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    
    install_requires=['py-pushover-open-client', 'CommandToDomoticz', 'requests'],
)
