from setuptools import setup

setup(name='openflow',
      version='0.1.2.2',
      description='Automate data flows for machine learning.',
      url='http://github.com/shoprunback/openflow',
      author='Quentin Lapointe',
      author_email='quentin@shoprunback.com',
      license='MIT',
      packages=['openflow'],
      install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'scipy'
      ],
      zip_safe=False)
