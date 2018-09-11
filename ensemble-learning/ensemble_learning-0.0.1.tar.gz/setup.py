import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ensemble_learning",
    version="0.0.1",
    author="Albert Calvo",
    author_email="albertc@cs.upc.edu",
    description="Ensemble Learning algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertcalv/ensemble_learning",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
