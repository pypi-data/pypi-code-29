from setuptools import setup

setup(name='pman_reaper',
      version='0.1',
      description='Reaper for pman jobs',
      author='Parul Singh',
      author_email='singh.p@husky.neu.edu',
      license='MIT',
      install_requires = ['kubernetes'],
      packages=['pman_reaper'],
      zip_safe=False)