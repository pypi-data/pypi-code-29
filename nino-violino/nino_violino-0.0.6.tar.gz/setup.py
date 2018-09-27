import setuptools

setuptools.setup(
  name='nino_violino',
  packages=['block_generator', 'block_generator.block_parser', 'block_generator.song_namer'],
  version='0.0.6',
  description='Yet another music generator. ',
  keywords=['nino_violino'],
  author='Nikola Dokoski',
  install_requires=[
    'midiutil',
    'haikunator',
  ],
)
