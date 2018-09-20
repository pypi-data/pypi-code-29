from setuptools import setup, find_packages
import os

setup(
    name='uperations-base',
    version='0.0.5',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'README.rst')).read(),
    author='Brice Aminou',
    author_email='brice.aminou@gmail.com',
    keywords='workflow tool',
    url='https://github.com/baminou/Uperations-Base'
)