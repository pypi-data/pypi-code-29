from setuptools import setup

setup(name='pykarma-subreddit',
      version='1.2',
      description="A python API for Karma Decay",
      url='https://github.com/Aculisme/pykarma',
      author='Sambhav Kothari',
      author_email='luca.mehl@gmail.com',
      license='MIT',
      packages=['pykarma-subreddit'],
      install_requires=[
          'praw',
          'beautifulsoup4',
      ])
