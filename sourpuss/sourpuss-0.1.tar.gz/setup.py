import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

install_requires = [
    'click',
    'pandas',
]

setup(name='sourpuss',
      version=version,
      description="Like feeding pickles to a cat(1)",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Text Processing :: General',
          'Topic :: Utilities',
      ],
      keywords='pandas cat pickle',
      author='Rhys Ulerich',
      author_email='rhys.ulerich@gmail.com',
      url='https://github.com/RhysU/sourpuss',
      license='Mozilla Public License 2.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={'console_scripts': ['sourpuss=sourpuss:main']},
      )
