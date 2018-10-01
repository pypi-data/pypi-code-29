from distutils.core import setup

setup(name='MeCabOnigiri',
      version='0.2.0',
      description='Python Distribution Utilities',
      author='uehara1414',
      author_email='akiya.noface@gmail.com',
      url='https://github.com/uehara1414/MeCabOnigiri',
      packages=['MeCabOnigiri'],
      install_requires=[
            'mecab-python3',
      ],
      )
