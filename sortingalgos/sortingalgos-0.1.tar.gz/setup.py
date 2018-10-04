from setuptools import setup

setup(name='sortingalgos',
      version='0.1',
      description='sorting algorithms',
      long_description='Really, sorting stuff',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/storborg/funniest',
      author='Faysal Zoubi',
      author_email='faysal@example.com',
      license='MIT',
      packages=['sortingalgos'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)