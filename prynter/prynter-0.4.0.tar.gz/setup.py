from setuptools import setup, find_packages
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()

main_ns = {}
ver_path = convert_path('prynter/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="prynter",
    version=main_ns['__version__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Iván Canales",
    author_email="kanales.contact@gmail.com",
    description="Small utility to execute short python commands",
    url="https://github.com/kanales/prynter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'prynt = prynter.__main__:main'
        ]
    }
)
