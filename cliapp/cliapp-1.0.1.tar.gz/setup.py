from distutils.core import setup
ver = '1.0.1'
setup(
    name='cliapp',
    packages=['cliapp'],  # this must be the same as the name above
    version=ver,
    description='a python2 cliapp framework',
    author='chang',
    author_email='zhchang@gmail.com',
    url='https://github.com/zhchang/cliapp',  # use the URL to the github repo
    download_url='https://github.com/zhchang/cliapp/tarball/' + ver,
    keywords=['python', 'cli', 'util'],  # arbitrary keywords
    classifiers=[],
)
