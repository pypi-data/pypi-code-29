import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PySlideShow",
    version="0.0.4",
    author="Thomas Ruland",
    author_email="PySlideShow@gmail.com",
    description="Configurable image slideshows.",
    long_description="Configurable image slideshows.",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/PySlideShow/pyslideshow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/PySlideShow.py'],
)
