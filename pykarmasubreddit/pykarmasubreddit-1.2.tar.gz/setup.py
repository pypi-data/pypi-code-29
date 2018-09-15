from setuptools import setup

setup(name='pykarmasubreddit',
      version='1.2',
      description="A python API for Karma Decay",
      url='https://github.com/Aculisme/pykarma',
      author='Aculisme',
      author_email='luca.mehl@gmail.com',
      license='MIT',
      packages=['pykarmasubreddit'],
      install_requires=[
          'praw',
          'beautifulsoup4',
      ])
