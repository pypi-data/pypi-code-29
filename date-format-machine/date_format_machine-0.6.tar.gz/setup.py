from __future__ import with_statement
from setuptools import setup

setup(
    name='date_format_machine',
    version='0.6',
    description='Tool for manipulating date strings',
    url='https://github.com/ryantownshend/date_format_machine',
    author='Ryan Townshend',
    author_email='citizen.townshend@gmail.com',
    install_requires=[
        'click>=7.0',
        'click-log>=0.3.2',
        'pendulum>=2.0.3',
        'tabulate>=0.8.2',
        'PyYAML>=3.13',
    ],
    py_modules=['dfm'],
    packages=['dfm'],
    package_data={
        'dfm':
            ['dfm_formats.yaml']
    },
    entry_points={
        'console_scripts': [
            'dfm = dfm.dfm:cli',
            'date_format_machine = dfm.dfm:cli',
        ],
    },
)
