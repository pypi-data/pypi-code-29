from setuptools import setup

# reading long description from file
# with open('DESCRIPTION.txt') as file:
#     long_description = file.read()


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

# calling the setup function
setup(name='hellobomma',
      version='1.0.4',
      description='An basic hello world program',
      long_description="use hello world function to test package",
      url='https://github.com/bomma-anil/hello-world.git',
      author='bomma.anil',
      author_email='bomma.anil@stackaero.com',
      license='MIT',
      packages=['sample'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='hello function'
      )
