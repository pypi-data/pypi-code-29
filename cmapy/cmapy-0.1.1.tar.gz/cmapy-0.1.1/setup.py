"""Export colormaps from Matplotlib so they can be used
(for exaple) with OpenCV.

See: https://gitlab.com/cvejarano-oss/cmapy/
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='cmapy',
      version='0.1.1',
      description='Export colormap data from Matplotlib.',
      long_description=long_description,
      author='Camilo Vejarano',
      license='MIT',
      py_moudles=['cmapy'],
      install_requires=['matplotlib', 'numpy'],
      project_urls={
            'Bug Reports': 'https://gitlab.com/cvejarano-oss/cmapy/issues/',
            'Source': 'https://gitlab.com/cvejarano-oss/cmapy/',
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
