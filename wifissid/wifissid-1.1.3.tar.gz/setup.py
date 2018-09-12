from distutils.core import setup
import setuptools



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wifissid",
    version="1.1.3",
    author="luxun",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/wifissid/",
    packages=setuptools.find_packages(),
    py_modules=['wifissid'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)