from setuptools import setup

setup(name='cryptocompy3',
      packages=['cryptocompy'],
      version='0.1.2',
      description='Simple wrapper for the public Cryptocompare API (maintenance fork of cryptocompy).',
      long_description='This is a maintenance fork of Titian Steiger\'s project.',
      keywords='',
      author='Sebastian Haberey',
      author_email='sebastian@haberey.com',
      url='https://github.com/sebastianhaberey/cryptocompy',
      download_url='https://github.com/sebastianhaberey/cryptocompy/archive/0.1.2.tar.gz',
      license='MIT',
      python_requires='>=3',
      install_requires=['requests'], )
