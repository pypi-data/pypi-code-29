from setuptools import setup

setup(
    name='migrator-2000',
    version='1.0',
    py_modules=['migrator'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        migrator=migrator:command
    '''
)