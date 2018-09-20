"""
Zinc Python Tools

A collection of Qt widgets and utilities building on the Python bindings for the OpenCMISS-Zinc Visualisation Library.
"""
from setuptools import setup

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Programming Language :: Python
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering :: Medical Science Apps.
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development :: Libraries :: Python Modules
"""

doc_lines = __doc__.split("\n")
requires = ['PySide', 'opencmiss.utils', 'PySideX']

setup(
    name='opencmiss.zincwidgets',
    author='H. Sorby',
    author_email='h.sorby@auckland.ac.nz',
    packages=['opencmiss', 'opencmiss.zincwidgets', 'opencmiss.zinchandlers'],
    platforms=['any'],
    url='https://github.com/OpenCMISS-Bindings/ZincPythonTools',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    description=doc_lines[0],
    classifiers=[],#filter(None, classifiers.split("\n")),
    install_requires=requires,
    zip_safe=False,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
