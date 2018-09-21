from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="dummy_wsgi_framework",
    version="0.0.19",
    author="BorisPlus",
    author_email="boris-plus@mail.ru",
    description="Dummy WSGI Framework is base for your Web-applications or your own WSGI-framework",
    long_description=long_description,
    url="https://github.com/BorisPlus/dummy_wsgi_framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
)
