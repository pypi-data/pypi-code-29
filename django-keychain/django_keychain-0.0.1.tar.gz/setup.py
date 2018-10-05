from setuptools import setup
from os import environ
setup(name='django_keychain',
      version="0.0.1",
      description='Django Keychain',
      author='Gregory Reshetniak',
      author_email='ror6ax@gmail.com',
      packages=['django_keychain'],
      install_requires=[
          'boto3',
      ],
)
