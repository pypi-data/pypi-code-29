from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(name='pygardena',
      version='0.0.13',
      author='Mikael Johansson',
      author_email='mikael@thematrix.se',
      url='https://github.com/liquid667/pygardena',
      description='Library to communicate with Gardena smart home products',
      long_description=readme,
      license=license,
      packages=find_packages(exclude=('tests')),
      classifiers=(
          "Programming Languate :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ))
