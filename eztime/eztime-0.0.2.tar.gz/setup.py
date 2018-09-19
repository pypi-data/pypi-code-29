from distutils.core import setup
setup(
  name = 'eztime',
  packages = ['eztime'], # this must be the same as the name above
  version = '0.0.2',
  description = 'A timer that easily integrates with functions and code chunks',
  author = 'Manifold.ai',
  author_email = 'jcarpenter@manifold.ai',
  url = 'https://github.com/manifoldai/eztime', # use the URL to the github repo
  download_url = 'https://github.com/manifoldai/eztime/archive/0.0.2.tar.gz',
  keywords = ['time', 'timer', 'function'],
  install_requires=[
      'functools',
      'contextlib',
      'logging'
  ],
  classifiers = [],
)
