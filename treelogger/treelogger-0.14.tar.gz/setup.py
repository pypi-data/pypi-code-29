from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='treelogger',
      version='0.14',
      description='Create tree structures for your logs',
      url='',
      author='Hong Yang',
      author_email='hong.meng.yang@outlook.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=['treelogger'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],

      )