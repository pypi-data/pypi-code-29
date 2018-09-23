from setuptools import setup, find_packages

setup(name='ocutils',
      version='1.1.1',
      description='Utility functions for oceanography related work',
      author='Marcus Donnelly',
      author_email='marcus.k.donnelly@gmail.com',
      license='BSD',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering'
                   ],
      keywords=['Oceanography',
                'Utilities',
                ],
      packages=find_packages(),
      install_requires=['numpy',
                        ],
      package_data={'ocutils': ['CM_coeffs.txt'],
                    },
      )
