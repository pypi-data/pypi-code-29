from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup(name='pyanimate',
      version='0.1',
      url='https://github.com/martinmcbride/pyanimate',
      license='MIT',
      author='Martin McBride',
      author_email='mcbride.martin@gmail.com',
      description='Create animated gifs, movies and images in Python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(exclude=['examples']),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      setup_requires=[])
