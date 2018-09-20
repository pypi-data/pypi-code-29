
"""A setuptools based setup module.
"""

from setuptools import setup, find_packages

setup(
    name='ridi-secret-keeper',
    packages=[
        'ridi.secret_keeper',
    ],
    version='0.1.1',
    description='Ridi Secret Keeper',
    url='https://github.com/ridi/secret-keeper',
    keywords=['secret', 'secret-keeper', 'ridi', 'ridibooks'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'boto3>=1.8.9',
    ],
)