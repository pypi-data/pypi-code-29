from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nn_calculator',
    packages=['calculator'],
    description='Simple application to teach CI/CD',
    long_description=long_description,
    version='0.4',
    url='https://gitlab.com/MvdLinden/nn-cicd',
    author='Marco van der Linden',
    author_email='mvanderlinden@xebia.com',
    keywords=['cicd', 'example']
    )
