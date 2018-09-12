from os import path
from setuptools import setup


def version():
    init = path.join(path.dirname(__file__), "gphotos", "__init__.py")
    line = list(filter(lambda l: l.startswith("__version__"), open(init)))[0]
    return line.split("=")[-1].strip(' "\n')


setup(name="gphotos",
      packages=["gphotos"],
      version=version(),
      author="Guillermo Guirao Aguilar",
      author_email="contact@guillermoguiraoaguilar.com",
      license="MIT",
      url="https://github.com/Funk66/gphotos",
      python_requires=">=3.6",
      classifiers=[
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
      ])
