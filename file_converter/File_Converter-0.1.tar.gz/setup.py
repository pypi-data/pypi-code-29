from distutils.core import setup
 
setup(
    name = 'File_Converter', # a unique name for PyPI
    version ='0.1',
    description = 'Make me them backups',
    author = 'Mitchell Sheep',
    author_email = 'mitch94ab@yahoo.com',
    url = 'http://lin-chen-va.github.io', # http://location or https://location
    packages = ['myPackage', ], # packages and subpackages containing .py files
    package_data = {'myPackage':['other/*']}, # other needed files will be installed for user
    scripts = ['mod3',], # the executable files will be installed for user
    license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description = open('README').read(),
    # more meta-data for repository
    classifiers = [
      'Development Status :: 4 - Beta',
      'Environment :: X11 Applications :: GTK',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX :: Linux',
      'Topic :: Desktop Environment',
      'Topic :: Text Processing :: Fonts'
      ],
)
