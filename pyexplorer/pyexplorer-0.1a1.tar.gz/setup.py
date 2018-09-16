import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyexplorer",
    version="0.1a1",
    author="Fabrizio Destro",
    author_email="destro.fabrizio@gmail.com",
    entry_points={
        'console_scripts': ["pyexplorer=pyexplorer.pyexplorer:main"]
    },
    description="Explore python modules interactively.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "termcolor",
        "prompt_toolkit",
        "future",
    ],
    url="https://github.com/dexpota/pyexplorer",
    packages=setuptools.find_packages(),
)
