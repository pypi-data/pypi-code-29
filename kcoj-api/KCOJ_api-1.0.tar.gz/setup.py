from setuptools import setup, find_packages

setup(
    name='KCOJ_api',
    version='1.0',
    description='A Python Module for get data from real KCOJ.',
    author='pinlin',
    author_email='moneycat711@gmail.com',
    license='MIT License',
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
    platforms=["all"],
    url='https://github.com/kcoj/KCOJ_api',)