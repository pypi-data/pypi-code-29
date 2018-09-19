from setuptools import setup

setup(
    name='ftredis',
    description='minimal wrapper for ebani module',
    url='https://github.com/pizdoc/ftredis',
    author='pizdoc',
    version='0.1.2',
    packages=['ftredis'],
    install_requires=['redis']
)