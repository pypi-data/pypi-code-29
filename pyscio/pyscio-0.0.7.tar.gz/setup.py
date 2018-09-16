from numpy.distutils.core import setup, Extension

module1 = Extension('scio_extension', sources=['pyscio/lib/scio.f90', 'pyscio/lib/scio_extension.pyf'])
long_description = """
Sparse Column-wise Inverse Operator for estimating the inverse covariance matrix.
Note that this is a preliminary version accompanying the arXiv paper (arXiv:1203.3896) in 2012.
This version contains only the minimal set of functions for estimation and cross validation.
"""

setup(
    name="pyscio",
    version="0.0.7",
    description="A Python wrapper for scio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    packages=['pyscio'],
    ext_modules=[module1]
)