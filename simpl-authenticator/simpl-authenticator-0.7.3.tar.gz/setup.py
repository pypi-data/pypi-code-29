import os
from setuptools import setup, find_packages

VERSION = '0.7.3'

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='simpl-authenticator',
    version=VERSION,
    description='WAMP Authenticator Component for Simpl',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/simplworld/simpl-authenticator',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        "autobahn==17.10.1",
    ],
    tests_require=[
    ]
)
