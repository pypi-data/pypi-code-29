from setuptools import setup, find_packages
import os
from lbryschema import __version__ as version

requires = [
    'protobuf==3.2.0',
    'jsonschema',
    'ecdsa',
    'cryptography'
]

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lbryschema")
setup(
    name="lbryschema",
    description="Protobuf schema for claims on the LBRY blockchain",
    version=version,
    author="jackrobison@lbry.io",
    install_requires=requires,
    packages=find_packages(exclude=['tests'])
)
