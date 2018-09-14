import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weichigong",
    version="1.0.0",
    author="dashixiong lee",
    author_email="dashixiong@gmail.com",
    description="a centralized configuration library based on zookeeper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perfeelab/weichigong",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
