from setuptools import setup, find_packages
from pathlib import Path
import os

here = Path(__file__).parent.absolute()
project_name = 'fyrgo'

setup(
    name = project_name,
    version        = __import__(project_name).__version__,
    author         = __import__(project_name).__author__,
    author_email   = __import__(project_name).__contact__,
    url = 'https://gitlab.oca.eu/crobert/fyrgo',
    description = 'Data frame and tools for FargOCA',
    license = 'GNU',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Database :: Front-Ends',
        'Programming Language :: Python :: 3.6'
    ],
    keywords = 'data analysis simulations',
    install_requires = [
        'numpy>=1.13.3',
        'matplotlib>=2.1.0',
        'pandas>=0.20.3'
    ],
    python_requires = '>=3.6',
    packages = find_packages(),
    package_data = {'fyrgo.utils': ['default_planet_format.in']},
    data_files = [('data', ['data/'+f for f in next(os.walk('data/'))[-1]])],
)
