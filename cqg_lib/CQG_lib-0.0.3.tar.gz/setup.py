import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CQG_lib",
    version="0.0.3",
    author="Nina Lin",
    author_email="ninal@cqg.com",
    description="A package to chart in CQG Integrated Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.denver.cqg/ninal/Boundfit.PythonNet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

