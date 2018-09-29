"""Our setup script."""

import sys
from setuptools import setup

long_description_header_text = "GF3: Lisp-Like Generic Functions For Python 3"
long_description_header_decoration = "=" * len(long_description_header_text)
long_description_header = "\n".join((
        long_description_header_decoration,
        long_description_header_text,
        long_description_header_decoration))
long_description_header += "\n"
try:
    with open("docs/overview.rst") as readme_file:
        long_description = (long_description_header + "\n" +
                readme_file.read())
    with open("docs/acknowledgements.rst") as readme_file:
        long_description += readme_file.read()
    long_description = long_description.replace(":class:", "").replace(
            ":func:", "").replace(":meth:", "")
except IOError:
    long_description = None

#d#print long_description

sys.path.insert(0, "tests")

setup(name="gf3",
      version='0.2.1',
      description="A package with lisp-like generic functions for python 3.",
      long_description = long_description,
      keywords="generic-function multi-method",
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Python Software Foundation License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: Implementation",
            "Topic :: Software Development :: Libraries",
      ],
      author="Gerald Klix",
      author_email="gf@klix.ch",
      packages=['gf'],
      url="http://gf3.klix.ch/",
      zip_safe=True,
      test_suite="testgo",
      license="PSF",
      )
