# https://pythonhosted.org/an_example_pypi_project/setuptools.html
# set HOME=c:\s\telos\python
# python setup.py sdist bdist_wininst upload.bat


from setuptools import setup, find_packages
import os

tests_require = ['unittest',  'pandas', 'matplotlib', 'sly']

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = r"""
What is aggregate?
------------------

**aggregate** is a Python package providing fast, accurate, and expressive data
structures designed to make working with probability distributions
easy and intuitive. Its primary aim is to be an educational tool, allowing
experimentation with complex, **real world** distributions. It has applications in
insurance, risk management, actuarial science and related areas.

Main Features
-------------

Here are just a few of the things that ``aggregate`` does well:

  - Output in tabular form using Pandas
  - Human readable persistence in YAML
  - Built in library of insurance severity curves for both catastrophe and non
    catastrophe lines
  - Built in parameterization for most major lines of insurance in the US, making it
    easy to build a "toy company" based on market share by line
  - Clear distinction between catastrophe and non-catastrohpe lines
  - Use of Fast Fourier Transforms throughout differentiates ``aggregate`` from
    tools based on simulation
  - Fast, accurate - no simulations!
  - Graphics and summaries following Pandas and Matplotlib syntax


Potential Applications
----------------------

  - Education
       * Building intuition around how loss distribtions convolve
       * Convergence to the central limit theorem
       * Generalized distributions
       * Compound Poisson distributions
       * Mixed distributiuons
       * Tail behavior based on frequency or severity tail
       * Log concavity properties
       * Uniform, triangular to normal
       * Bernoulli to normal = life insurance
       * $P(A>x)\sim \lambda P(X>x) \sim P(M>x)$ if thick tails
       * Occ vs agg PMLs, body vs. tail. For non-cat lines it is all about correlation; for cat it is all about the tail
       * Effron's theorem
       * FFT exact for "making" Poisson, sum of normals is normal, expnentials is gamma etc.
       * Slow convergence of truncated stable to normal
       * Severity doesn't matter: difference between agg with sev and without for large claim count and stable severity
       * Small large claim split approach...attrit for small; handling without correlation??
       * Compound Poisson: CP(mixed sev) = sum CP(sev0
  - Pricing small insurance portfolios on a claim by claim basis
  - Analysis of default probabilities
  - Allocation of capital and risk charges
  - Detailed creation of marginal loss distributions that can then be
    sampled and used by other simulation software, e.g. to incorporate
    dependence structures, or in situations where it is necessary to
    track individual events, e.g. to compute gross, ceded and net bi-
    and trivariate distributions.


Practical Modeling Examples
---------------------------

* From limit profile
* Mixed severity
* Modeling $N\mid N \ge n$
* How to model 2 reinstatements



Missing Features
----------------

Here are some important things that ``aggregate`` does **not** do:

  - It is strictly univariate. It is impossible to model bivariate or multivariate distributions.
    As a result ``aggregate`` is fast and accurate
  - ``aggregate`` can model correlation between variables using shared mixing variables. This
    is adequate to build realistic distributions but would not be adequate for an industrial-
    strength insurance company model.

Documentation
-------------

http://www.mynl.com/aggregate/documentation.html


Where to get it
---------------

* The source code is currently hosted on GitHub at:
* https://github.com/mynl/aggregate


Dependencies
------------

- [NumPy](https://www.numpy.org): 1.9.0 or higher
- [Pandas](https://github.com/pandas-dev/pandas): 0.23.0 or higher

License
-------

[BSD 3](LICENSE)
"""

setup(name="aggregate",
      description="aggregate - working with compound probability distributions",
      long_description=long_description,
      license="""BSD""",
      version="0.5",
      author="Stephen J. Mildenhall",
      author_email="mildenhs@stjohns.edu",
      maintainer="Stephen J. Mildenhall",
      maintainer_email="mildenhs@stjohns.edu",
      packages=['aggregate'],
      package_data={'': ['*.txt', '*.rst', 'yaml/*.yaml', 'examples/*.py', 'examples/*.ipynb',
                        'test/*.py']},
      tests_require=tests_require,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: BSD License',
          'Topic :: Education',
          'Topic :: Office/Business :: Financial',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Education'
      ],
      project_urls={"Documentation": 'http://www.mynl.com/aggregate/',
                    "Source Code": "https://github.com/mynl/aggregate"}
      )
