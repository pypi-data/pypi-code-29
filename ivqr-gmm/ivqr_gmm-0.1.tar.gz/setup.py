import setuptools

with open("README.md", "r") as f:
      long_discription = f.read()

setuptools.setup(
      name='ivqr_gmm',
      packages=['ivqr_gmm'],
      version='0.1',
      description='Using GMM method to calculate the instrument variable quantile regression model proposed by Chen and Lee (2018).',
      long_discription = long_discription,
      url='https://github.com/jordanxzz/IVQR-GMM-Python-codes',
      author='Zizhe Xia',
      author_email='xiazizhejordan@gmail.com',
      classifiers = ['Programming Language :: Python :: 3.6'],
      python_requires='==3.6.*',
      zip_safe=False)
