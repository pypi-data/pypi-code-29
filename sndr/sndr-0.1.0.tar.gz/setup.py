import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sndr",
    version="0.1.0",
    author="Rodolfo Castilll Mateluna",
    author_email="rodolfocastillomateluna@gmail.com",
    description="Super simple json request wrapper over TCP (to be used with rcvr)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
