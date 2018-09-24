import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fio",
    version="0.0.05",
    author="Sumner Magruder",
    author_email="sumner.magruder@zmnh.uni-hamburg.de",
    description="Feature I/O for TensorFlow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/SumNeuron/fio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
