from distutils.core import setup
 
setup(
    name='ECSUConvert_1', # a unique name for PyPI
    version='0.5',
    description='Demo for building a Python project',
    author='Edsel Norwood',
    author_email='ebnorwood538@students.ecsu.edu',
    url='http://www.ecsu.edu', # http://location or https://location
    packages=['myPackage', 'myPackage/main', ], # packages and subpackages containing .py files
    package_data={'myPackage':['other/*']}, # other needed files will be installed for user
    scripts=['convert',], # the executable files will be installed for user
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README').read(),
    # more meta-data for repository
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: X11 Applications :: GTK',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Topic :: Desktop Environment',
      'Topic :: Text Processing :: Fonts'
      ],
)
