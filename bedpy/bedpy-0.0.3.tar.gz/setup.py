import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bedpy",
    version="0.0.3",
    author="Sumner Magruder",
    author_email="sumner.magruder@zmnh.uni-hamburg.de",
    description="Making bed files computable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/SumNeuron/bedpy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
