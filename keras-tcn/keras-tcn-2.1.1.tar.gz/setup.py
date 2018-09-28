from setuptools import setup

setup(
    name='keras-tcn',
    version='2.1.1',
    description='Keras TCN',
    author='Philippe Remy',
    license='MIT',
    long_description=open('README.md').read(),
    packages=['tcn'],
    # manually install tensorflow or tensorflow-gpu
    install_requires=['numpy',
                      'keras']
)
