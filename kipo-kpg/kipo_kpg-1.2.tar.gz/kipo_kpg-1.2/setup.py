import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kipo_kpg",
    version="1.2",
    author="Ali Abedi",
    author_email="ali@idco.io",
    description="Python Kipo KPG Library make it easy to stablish payment with kipo gateway.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kipolaboratory/kipo-kpg-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)