import versioneer
from setuptools import setup


with open('README.rst', 'r') as fh:
    long_description = fh.read()


setup(
    name='aerial',
    packages=['aerial'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='The easy way to catch signals',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Chris Brake',
    author_email='chris.brake@gmail.com',
    url='https://github.com/chrisbrake/aerial',
    keywords=['aerial', 'signals', 'signal', 'unix', 'sighup', 'sigterm'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ],
)
