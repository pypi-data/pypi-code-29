from distutils.core import setup
setup(
    name='seepy',
    version='0.6.2',
    description='Easy and fast dynamic report generation with Python',
    long_description = open("README.txt").read(),
    author='Lukasz Laba',
    author_email='lukaszlab@o2.pl',
    url='https://bitbucket.org/lukaszlaba/seepy',
    packages=['seepy', 'seepy.icons', 'seepy.examples', 'seepy.memos', 'seepy.pycore', 'seepy.templates'],
    package_data = {'': ['*.png', '*.md', '*.svg', '*.dxf']},
    license = 'GNU General Public License (GPL)',
    keywords = 'notebook ,script, report',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        ],
    )
