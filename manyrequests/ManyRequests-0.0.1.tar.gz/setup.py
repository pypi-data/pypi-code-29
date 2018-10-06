import setuptools

with open("ReadMe.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ManyRequests",
    version="0.0.1",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="A library to make many requests concurrently.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)