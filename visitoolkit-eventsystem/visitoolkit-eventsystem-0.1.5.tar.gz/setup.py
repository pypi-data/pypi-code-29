from setuptools import setup



# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='visitoolkit-eventsystem',
    version='0.1.5',
    packages=['visitoolkit_eventsystem'],
    url='https://github.com/stefanbraun-private/visitoolkit_eventsystem',
    license='GPL-3.0',
    author='Stefan Braun',
    author_email='sbraun@datacomm.ch',
    description=' minimalistic event system (a bag of handlers) ',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
