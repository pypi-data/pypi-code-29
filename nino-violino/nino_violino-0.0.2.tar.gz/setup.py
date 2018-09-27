import setuptools

setuptools.setup(
  name='nino_violino',
  packages=['block_generator'],
  version='0.0.2',
  description='Yet another music generator. ',
  keywords=['nino_violino'],
  author='Nikola Dokoski',
  install_requires=[
    'midiutil',
    'haikunator',
  ],
)
