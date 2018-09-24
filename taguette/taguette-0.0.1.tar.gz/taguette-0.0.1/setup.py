import io
import os
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))


with io.open('README.rst', encoding='utf-8') as fp:
    description = fp.read()
setup(name='taguette',
      version='0.0.1',
      py_modules=['taguette'],
      description="Document tagger for qualitative analysis",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      maintainer="Remi Rampin",
      maintainer_email='remirampin@gmail.com',
      url='https://taguette.fr/',
      project_urls={
          'Homepage': 'https://taguette.fr/',
          'Say Thanks': 'https://saythanks.io/to/remram44',
          'Source': 'https://gitlab.com/remram44/taguette',
          'Tracker': 'https://gitlab.com/remram44/taguette/issues',
      },
      long_description=description,
      license='BSD-3-Clause',
      keywords=['qualitative', 'document', 'text', 'tagging', 'tags',
                'highlights', 'notes'],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: JavaScript',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Text Processing'])
