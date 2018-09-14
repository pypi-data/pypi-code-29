import setuptools

__version__ = '1.0.11'

setuptools.setup(
    name="bot-test-repo",
    version=__version__,
    author="Jan Koscielniak",
    author_email="jkosciel@redhat.com",
    description="A small example package",
    long_description="Test",
    long_description_content_type="text/markdown",
    url="https://github.com/kosciCZ/bot-test-repo",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
