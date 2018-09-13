from setuptools import setup

setup(name='worin',
      version='0.1.0',
      description='A Korean POS Tagger using Neural Network',
      author='YU Jaemyoung',
      author_email='yu@mindscale.kr',
      url='https://github.com/mindscale/worin',
      packages=['worin'],
      package_data={
          '': ['*.txt', '*.md'],
          'worin': ['*.hdf5'],
      },
      install_requires=[
          'h5py',
          'numpy',
          'tensorflow',
      ],
      entry_points={
      },
      )
