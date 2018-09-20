from distutils.core import setup
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="networklib",
    version="0.0.6",
    description="download and upload flv,images",
    long_description=long_description,
    long_description_content_type="text/markdown",

    license = "MIT",
    author="zhaomingming",
    author_email="13271929138@163.com",
    url="http://www.zhaomingming.cn",
    py_modules=['networklib'],
    platforms = 'any'
)
