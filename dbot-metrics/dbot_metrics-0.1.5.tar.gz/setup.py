import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbot_metrics",
    version="0.1.5",
    author="xiaoch05",
    author_email="xiaoch2010@gmail.com",
    description="ATN atn dbot metrics package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ATNIO/metrics",
    packages = setuptools.find_packages(),
    install_requires=["leveldb >= 0.194"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
