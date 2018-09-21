import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unapid",
    version="0.0.1",
    author="Charles Kawczynski",
    author_email="kawczynski.charles@gmail.com",
    description="Prints some useful tables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/charliekawczynski/unapid",
    install_requires=[
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)