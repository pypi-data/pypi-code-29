import setuptools

setuptools.setup(
  name='nino_violino',
  packages=['block_generator', 'block_generator.block_parser'],
  version='0.0.4',
  description='Yet another music generator. ',
  keywords=['nino_violino'],
  author='Nikola Dokoski',
  install_requires=[
    'midiutil',
    'haikunator',
  ],
)
