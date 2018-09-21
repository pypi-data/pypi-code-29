from setuptools import setup

setup(name='mariasql',
      version='4',
      description='MariaDB/MySQL query builder primary for inserting and updating Python dictionaries into tables.',
      url='https://git.osuv.de/m/mariasql',
      author='Markus Bergholz',
      author_email='markuman@gmail.com',
      license='WTFPL',
      packages=['mariasql'],
      install_requires=[
          'pymysql',
      ],
      long_description=open('README.md').read(),
      zip_safe=False)
