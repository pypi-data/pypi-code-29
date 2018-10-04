"""Export colormaps from Matplotlib so they can be used
(for exaple) with OpenCV.

See: https://gitlab.com/cvejarano-oss/cmapy/
"""


from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='cmapy',
      version='0.1.8',
      description='Use Matplotlib colormaps with OpenCV in Python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://gitlab.com/cvejarano-oss/cmapy/',
      author='Camilo Vejarano',
      license='MIT',
      py_modules=['cmapy'],
      python_requires='>=3',
      install_requires=['matplotlib', 'numpy'],
      project_urls={
            'Bug Reports': 'https://gitlab.com/cvejarano-oss/cmapy/issues/',
            },
      classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research ",
            "Topic :: Multimedia :: Graphics",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Visualization",
            ],
      )
