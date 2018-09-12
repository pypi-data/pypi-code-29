from setuptools import setup

setup(
    name='manoc',
    version='1.2.4',
    packages=['manoc', 'manoc.commands', 'manoc.utils'],
    include_package_data=True,
    install_requires=[
        'click',
        'configparser',
        'requests',
        'prettytable',
        'jmespath'
    ],
    entry_points='''
        [console_scripts]
        manoc=manoc.cli:cli
    ''',
)
