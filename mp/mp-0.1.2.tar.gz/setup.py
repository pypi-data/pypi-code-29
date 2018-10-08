from setuptools import find_packages, setup

import mp


setup(name='mp',
      version=mp.__version__,
      description=mp.__doc__,
      long_description=mp.__doc__,  # TODO
      url='https://github.com/kerryeon/mp',
      author='kerryeon',
      author_email='besqer996@gnu.ac.kr',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          ],
      zip_safe=False,
      )
