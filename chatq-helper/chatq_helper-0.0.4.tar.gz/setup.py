from setuptools import setup
import os

setup(name='chatq_helper',
      version=os.environ['GIT_TAG'],
      description='chatq_helper',
      url='https://github.com/ChatQSG/chatq-helping-hand',
      author='ChatQ',
      author_email='',
      packages=['chatq_helper'],
      install_requires=['paho-mqtt==1.3.1'],
      zip_safe=False)