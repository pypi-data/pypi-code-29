from setuptools import setup

# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(name='hellopackage',
      version='0.0.1',
      description='The is an simple hello world program',
      long_description="long_description",
      url='https://github.com/bomma-anil/hellopackage.git',
      author='bomma.anil',
      author_email='bomma.anil@stackaero.com',
      license='MIT',
      packages=['hellopackage'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='hello function',
      )
