from setuptools import setup, find_packages

# Get the long description from the relevant file
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='charlotte_db',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.9.0',

    description='A lighting fast SDK for a lighting fast DB',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Danlobaton/flash-Charlotte-docs',

    # Author details
    author='Daniel A. Lobaton',
    author_email='dlobaton2@gmail.com',

    # Choose your license
    license='MIT',

    # See https://PyPI.python.org/PyPi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2.7,3.4',
    ],
    packages=find_packages(),
    install_requires=[
          'numpy>=1.12.1',
          'tensorflow>=1.1.0'
      ],

    # What does your project relate to?
    keywords='SDK',
)