from setuptools import setup

DISTNAME = 'scikit-grni'
VERSION = '0.1.03'
DESCRIPTION = "A set of modules for simplifying gene regulatory network inference, a branch of machine learning focused towards the problem of uncovering biological function from biological measurements."
# with open('README.rst') as f:
#     LONG_DESCRIPTION = f.read()
MAINTAINER = 'Andreas Tjärnberg'
MAINTAINER_EMAIL = 'andreas.tjarnberg@fripost.org'
URL = 'https://gitlab.com/Xparx/scikit-grni'
DOWNLOAD_URL = 'https://pypi.org/project/scikit-grni/#files'
LICENSE = 'LGPL'


setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      license=LICENSE,
      packages=['skgrni', 'gsexamples'],
      python_requires='>=3',
      install_requires=[
          'numpy',
          'pandas',
          'sklearn',
          'scipy',
          'fisher',
      ],
      zip_safe=False)
