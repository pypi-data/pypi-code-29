from setuptools import find_packages, setup

setup(
    name='python_utopian_rocks',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/yucealiosman/python-utopian-rocks',
    license='MIT',
    author='Ali Osman Yuce',
    author_email='aliosmanyuce@gmail.com',
    description='An API wrapper for utopian.rocks',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ),
)