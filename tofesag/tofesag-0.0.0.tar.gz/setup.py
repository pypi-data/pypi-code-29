import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='tofesag',
    packages=[
        'webtest29801923',
    ],
    scripts=[
        'webtest29801923/test1.py'
    ],
    include_package_data=True,
    install_requires=[
    ],
    requires=[
        'webtest'
    ]
)
