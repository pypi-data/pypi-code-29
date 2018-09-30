import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyRemoteConsole",
    version="0.0.2",
    author="py-am-i",
    author_email="duckpuncherirl@gmail.com",
    description="A pure Python 3 package containing hooks for running remote python consoles to interact with running scripts in real time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wykleph/PyRemoteConsole",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
