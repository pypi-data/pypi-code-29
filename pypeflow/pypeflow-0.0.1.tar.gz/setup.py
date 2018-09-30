import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypeflow",
    version="0.0.1",
    author="Sara Z.",
    author_email="bitit1994@gmail.com",
    description="Data pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xinyi2016/pypeflow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)