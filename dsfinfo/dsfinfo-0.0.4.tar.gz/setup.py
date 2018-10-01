import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsfinfo",
    version="0.0.4",
    author="Jim Knudstrup",
    author_email="jim.knudstrup@gmail.com",
    description="Run the info() method to disply Data Science Foundations links.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jknudstrup/dsf_info",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)