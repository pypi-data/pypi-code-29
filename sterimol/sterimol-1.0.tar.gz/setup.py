from setuptools import setup
setup(
  name = 'sterimol',
  packages = ['sterimol'],
  version = '1.0',
  description = 'A Command-Line Tool to Calculate Sterimol Parameters from Sructure Input/Output Files',
  author = 'Robert Paton',
  author_email = 'robert.paton@colostate.edu',
  url = 'https://github.com/bobbypaton/sterimol',
  download_url = 'https://github.com/bobbypaton/Sterimol/archive/v1.0.zip',
  keywords = ['cone-angles','sterimol','sterimol-parameters','organic-chemistry','conformational-analysis','qsar','sterics','gaussian'],
  classifiers = [],
  install_requires=["numpy","scipy"],
  python_requires='>=2.6',
  include_package_data=True,
)

