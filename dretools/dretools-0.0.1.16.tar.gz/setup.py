from __future__ import print_function
from setuptools import setup, find_packages
import io
from dretoolslib import version

if __name__ == "__main__":

    # from http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
    def read(*file_names, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')
        sep = kwargs.get('sep', '\n')
        buf = []
        for filename in file_names:
            with io.open(filename, encoding=encoding) as f:
                buf.append(f.read())
        return sep.join(buf)

    long_description = read('README.txt')

    # MAJOR version when they make incompatible API changes,
    # MINOR version when they add functionality in a backwards-compatible manner, and
    # MAINTENANCE version when they make backwards-compatible bug fixes.
    # http://semver.org/
    #
    # How to update of pypi
    # python3 setup.py sdist bdist_wheel
    # twine upload --repository-url https://upload.pypi.org/legacy/   dist/dretools-0.0.1.12*
    setup(
        name="dretools",
        version=version,
        author='Tyler Weirick',
        author_email='tyler.weirick@gmail.com',
        packages=find_packages(),
        license='CC BY 4.0',
        url="https://bitbucket.org/dretools/dretools",
        description='A software package for finding differential RNA editing.',
        long_description=long_description,
        platforms='any',
        scripts=['dretools'],
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        install_requires=[
            # Used with the program.
            'numpy>=1.9.2',
            'rpy2>=2.9.3',
            'scipy>=0.16.0',
            'statsmodels>=0.8.0',
            'intervaltree>=2.1.0',
            'scikit-learn>=0.16.1',
            'pysam>=0.13',
            'pandas>=0.19.0',
            # For testing.
            'behave',
            # 'mock'
        ]
    )

