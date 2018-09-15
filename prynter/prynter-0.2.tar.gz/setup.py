import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prynter",
    version="0.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Iván Canales",
    author_email="kanales.contact@gmail.com",
    description="Small utility to execute short python commands",
    url="https://github.com/kanales/prynter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
