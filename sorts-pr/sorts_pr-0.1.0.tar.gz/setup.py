from setuptools import setup

setup(name='sorts_pr',
      version='0.1.0',
      description='four sorting functions',
      long_description='includes 4 sorting functions bubble sort, selection sort, insertion sort and quick sort',
      keywords='sort bubble selection insertion quick',
      url='https://gitlab.propulsion-home.ch/pascal_rueegger/daily_work/tree/week3day4/week3/day4/sorts_pr',
      author='Pascal Rueegger',
      author_email='pascalrueegger@gmx.ch',
      license='MIT',
      packages=['sorts_pr'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )