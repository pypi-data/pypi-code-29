from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-set-ings',
    version='0.1.0',
    description='Load configuration from the environment for your python app.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/evocount/python-set-ings',
    author='Till Theato',
    author_email='till.theato@evocount.de',
    license='MIT',

    # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    python_requires='>=3.6',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # install_requires=[],

    extras_require={
        'test': [
            'pytest',
            'pytest-cov'
        ],
    },
)
