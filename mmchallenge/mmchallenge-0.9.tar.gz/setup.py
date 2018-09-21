from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='mmchallenge',
      packages=['mmchallenge'],
      version='0.9',
      description='Challenge package for MagicMakers Python',
       classifiers=[
        'Programming Language :: Python :: 3.7'],
      author='Team_Conception',
      author_email='guillaume.dupuy@magicmakers.fr',
      license='MagicMakers',
      include_package_data=True,
      install_requires=['cryptography' ,'pillow', 'birdy', 'spotipy', 'flask', 'foxdot', 'requests','opencv-python', 'termcolor', 'colorama', 'ffmpeg-python'],
      zip_safe=False)
