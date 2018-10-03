try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='cubepay',
      version='1.0.3',
      description='CubePay API library for Python, a third-party cryptocurrency payment gateway. https://cubepay.io',
      url='https://github.com/CubePayIO/cubepay-python',
      author='CubePayIO',
      author_email='service@cubepay.io',
      packages=['cubepay'],
      install_requires=['requests'],
      )
