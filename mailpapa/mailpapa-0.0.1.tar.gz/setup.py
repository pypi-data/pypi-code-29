import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailpapa",
    version="0.0.1",
    author="Maina Nick",
    author_email="contact@nickmaina.com",
    description="Search for emails in the wild",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mainanick/mailpapa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)