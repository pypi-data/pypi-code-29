import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_multiprocess_crawler",
    version="1.5.2",
    author="Jákob Rolík",
    author_email="rolik.jakob@gmail.com",
    description="Python BaseClass for easier multiprocess web-crawling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kvintus/python_multiprocess_crawler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Artistic License",
        "Operating System :: OS Independent",
    ],
)