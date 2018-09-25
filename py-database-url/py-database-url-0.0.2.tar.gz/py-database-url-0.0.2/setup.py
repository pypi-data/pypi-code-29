from setuptools import find_packages, setup

setup(
    name="py-database-url",
    description="A universal DATABASE_URL parser for Python.",
    version="0.0.2",
    url="https://github.com/jairojair/py-database-url",
    license="MIT",
    author="Jairo Jair",
    author_email="jairojair@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    extras_require={"dev": [open("dev-requirements.txt").read()]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
)
