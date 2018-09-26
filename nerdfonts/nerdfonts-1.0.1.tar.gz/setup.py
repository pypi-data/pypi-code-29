import setuptools

VERSION = "1.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nerdfonts",
    packages=setuptools.find_packages(),
    version=VERSION,
    description="Nerd Fonts for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GPLv3",
    author="Ajeet D'Souza",
    author_email="98ajeet@gmail.com",
    maintainer="Ajeet D'Souza",
    maintainer_email="98ajeet@gmail.com",
    url="https://gitlab.com/ajeetdsouza/nerdfonts-python",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Programming Language :: Python"
    ]
)
