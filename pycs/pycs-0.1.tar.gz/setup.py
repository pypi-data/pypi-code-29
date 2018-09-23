from setuptools import setup

setup(name='pycs',
      version='0.1',
      description='Basic data structures and algorithms',
      url='http://github.com/DanielLenz/pycs',
      author='Daniel Lenz',
      author_email='mail@daniellenz.org',
      license='MIT',
      packages=[
          'pycs',
          'pycs.datastructures',
          'pycs.algorithms',
          ],
      zip_safe=False)