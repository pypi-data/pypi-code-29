import setuptools
from setuptools import setup

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(name='torch-salad',
      version='0.1.4-alpha',
      description='Semi-supervised Adaptive Learning Across Domains',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://salad.domainadaptation.org',
      author='Steffen Schneider',
      author_email='steffen.schneider@tum.de',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ],
)