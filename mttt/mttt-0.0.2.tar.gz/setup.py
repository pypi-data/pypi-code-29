import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mttt",
    version="0.0.2",
    author="alex",
    author_email="a@b.com",
    description="Minimalist timetracking tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FeedTheWeb/mttt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

