import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fitchain",
    version = "0.0.17",
    author = "Fitchain",
    author_email = "hello@fitchain.io",
    description = "Fitchain Python Client",
    license = "Proprietary",
    keywords = "fitchain data client",
    url = "https://bitbucket.org/fitchain/fitchain-sdk-python",
    packages=['fitchain'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires=[
        'pandas',
        'numpy',
        'faker',
        'requests',
        'pyyaml',
        'joblib',
        'filemagic',
        'pprint',
        'keras',
        'Pillow',
    ],
)
