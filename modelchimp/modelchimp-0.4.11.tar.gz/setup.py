from setuptools import setup

setup(
  name = 'modelchimp',
  packages = ['modelchimp'],
  version = '0.4.11',
  description = 'Python client to upload the machine learning models data to the model chimp cloud',
  author = 'Samir Madhavan',
  author_email = 'samir.madhavan@gmail.com',
  url = 'https://www.modelchimp.com',
  keywords = ['modelchimp', 'ai', 'datascience'],
  install_requires=[
          'requests',
          'future',
          'six',
          'websocket-client',
          'pytz',
          'cloudpickle'
      ],
  classifiers = [],
)
