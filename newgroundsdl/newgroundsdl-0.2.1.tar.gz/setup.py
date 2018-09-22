import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newgroundsdl",
    version="0.2.1",
    author="Nonny Moose",
    author_email="moosenonny10@gmail.com",
    description="A simple package to download songs from Newgrounds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/nonnymoose/newgroundsdl",
    packages=setuptools.find_packages(),
    python_requires=">=3",
    install_requires=["beautifulsoup4"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Development Status :: 5 - Production/Stable"
    ],
    scripts=["newgroundsdl/newgroundsdl"]
)
