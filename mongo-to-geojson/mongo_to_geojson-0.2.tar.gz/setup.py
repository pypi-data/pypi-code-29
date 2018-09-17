from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mongo_to_geojson',
      version='0.2',
      description='extract geojson from Mongo',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='mongo geojson',
      url='https://github.com/westchamp24/mongo_to_geojson',
      author='Rafael Ferraro',
      author_email='rafael.m.ferraro@gmail.com',
      license='MIT',
      packages=['mongo_to_geojson'],
      install_requires=[
          'click>=6.7',
          "pymongo>=3.7.1"
      ],
      entry_points={
          'console_scripts': ['mongo2geojson=mongo_to_geojson.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)