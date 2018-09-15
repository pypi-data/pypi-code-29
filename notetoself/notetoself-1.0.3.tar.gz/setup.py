from setuptools import setup, find_packages

from nts import __version__


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="notetoself",
    version=__version__,
    description="Note To Self -- Quick note taking tool",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    keywords="note",
    url="https://gitlab.com/admicos/nts",
    author="Ecmel B. CANLIER",
    author_email="me@ecmelberk.com",
    license="Apache License Version 2.0",
    packages=find_packages(),
    py_modules=['notetoself'],
    install_requires=["appdirs", "colorama", "commonmark<0.8.0", "consolemd"],
    entry_points={
        'console_scripts': ['nts=notetoself:run'],
    },
    include_package_data=True,
    zip_safe=False,
)
