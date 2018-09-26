from setuptools import setup

setup(name='pyarks',
      version='0.1',
      description='A package to get wait times from amusement parks',
      url='http://github.com/joshimbriani/Pyarks',
      download_url='https://github.com/joshimbriani/Pyarks/archive/v0.1.tar.gz',
      author='Josh Imbriani',
      author_email='pypi@joshimbriani.com',
      license='MIT',
      packages=['pyarks'],
      install_requires=[
            'requests',
            'arrow'
      ],
      zip_safe=False)