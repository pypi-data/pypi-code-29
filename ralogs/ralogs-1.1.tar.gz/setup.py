from setuptools import setup

setup(
    name='ralogs',
    version='1.1',
    url='https://github.com/barell/ralogs',
    packages=['ralogs',],
    license='MIT',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'ralogs=ralogs.ralogs:main'
        ]
    },
)