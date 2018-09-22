import io
import os
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))


description = '''\
Document tagger
===============

This project aims at creating an open-source document tagger, for use in qualitative data analysis.
'''

setup(name='taguette',
      version='0.0',
      py_modules=['taguette'],
      description="Document tagger",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      maintainer="Remi Rampin",
      maintainer_email='remirampin@gmail.com',
      url='https://gitlab.com/remram44/taguette',
      project_urls={
          'Homepage': 'https://taguette.fr/',
          'Say Thanks': 'https://saythanks.io/to/remram44',
          'Source': 'https://gitlab.com/remram44/taguette',
          'Tracker': 'https://gitlab.com/remram44/taguette/issues',
      },
      long_description=description,
      license='BSD-3-Clause',
      keywords=['qualitative', 'qual', 'document', 'text', 'tagging', 'tags',
                'highlight', 'highlights', 'notes'],
      classifiers=[
          'Development Status :: 1 - Planning',
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
