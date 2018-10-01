try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
    'description': 'Module to access azure blob CSV files with Pandas',
    'author': 'Neelabh Kashyap',
    'url': 'https://github.com/nihil0/bluepandas',
    'author_email': 'neelabh.kashyap@cgi.com',
    'version': '0.2',
    'install_requires': ['azure-storage-blob', 'pandas'],
    'packages': find_packages(exclude=['contrib', 'docs', 'tests']),
    'scripts': [],
    'name': 'bluepandas',
    'classifiers': [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
}

setup(**config)