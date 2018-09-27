import setuptools
from distutils.core import setup

setup(
    name='angrop',
    version='7.8.9.26',
    python_requires='<3.0',
    description='The rop chain builder based off of angr',
    packages=['angrop'],
    install_requires=[
        'progressbar==2.3',
        'angr==7.8.9.26',
        'pyvex==7.8.9.26',
        'claripy==7.8.9.26',
    ],
)
