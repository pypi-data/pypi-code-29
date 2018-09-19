from setuptools import setup

setup(name='falcon-prometheus',
      description='Falcon Framework Prometheus Middleware',
      version='0.1.0',
      url='https://gitlab.com/shdh/falcon-prometheus',
      author='Shawn Dhawan',
      author_email='me@shdh.ca',
      license='MIT',
      packages=['falcon_prometheus'],
      install_requires=[
          'falcon',
          'prometheus_client>=0.3.1'
      ],
      scripts=[],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: System :: Monitoring',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
          'License :: OSI Approved :: MIT License'
      ]
)
