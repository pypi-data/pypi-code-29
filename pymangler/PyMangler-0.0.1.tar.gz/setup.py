import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyMangler",
    version="0.0.1",
    author="py-am-i",
    author_email="duckpuncherirl@gmail.com",
    description="PyMangler contains a pure-python \"encryption\" scheme that can be used to *obfuscate* and *disguise* datain situations where strong encryption is not available,and security is not necessarily top priority.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wykleph/PyMangler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
