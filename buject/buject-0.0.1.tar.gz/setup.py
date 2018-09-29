import setuptools
import buject

with open("readme.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=buject.name,
    version=buject.__version__,
    author="Razgovorov Mikhail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['buject'],
    classifiers=[
    ],
)
