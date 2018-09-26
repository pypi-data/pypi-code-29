from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='thread_processor',
    version='0.2',
    description="Execute function for each argument through a fixed number of threads",
    long_description=long_description,
    url='https://github.com/krishnabhupatiraju/thread_processor',
    author='Krishna Bhupatiraju',
    author_email='krishnavarma@gmail.com',
    license='MIT',
    packages=['thread_processor'],
    zip_safe=True
)
