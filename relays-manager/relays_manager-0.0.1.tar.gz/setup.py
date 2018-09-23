from setuptools import setup

setup(
    name='relays_manager',
    version='0.0.1',
    packages=['relays_manager'],
    install_requires=[
        'pyserial',
    ],
    url='https://github.com/M-Gregoire/relays_manager',
    keywords=['relays'],
    classifiers=[],
    author='Grégoire Martinache',
    description='A Python library to interact with ICStation USB relays.'
)
