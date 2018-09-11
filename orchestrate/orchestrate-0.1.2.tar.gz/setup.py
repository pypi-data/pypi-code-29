from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from orchestrate.version import VERSION


install_requires = [
  'boto3==1.7.33',
  'cement==2.10.12',
  'colorama==0.3.9',
  'docker==3.4.1',
  'pystache==0.5.4',
  'PyYAML==3.12',
  'requests==2.19.1',
  'sigopt==3.2.0',
  'six==1.11.0',
]

def post_installation():
  import hashlib
  from orchestrate.core.paths import (
    check_iam_authenticator_executable,
    check_kubectl_executable,
    download_kubectl_executable,
    download_iam_authenticator_executable,
    get_bin_dir,
    ensure_dir,
  )

  ensure_dir(get_bin_dir())

  for check, download in [
    (check_kubectl_executable, download_kubectl_executable),
    (check_iam_authenticator_executable, download_iam_authenticator_executable),
  ]:
    try:
      check()
    except Exception as e:
      download()
      check()

class PostDevelopCommand(develop):
  def run(self):
    post_installation()
    develop.run(self)

class PostInstallCommand(install):
  def run(self):
    post_installation()
    install.run(self)

setup(
  name='orchestrate',
  version=VERSION,
  description='SigOpt Orchestrate Client',
  author='SigOpt',
  author_email='support@sigopt.com',
  url='https://sigopt.com/docs/orchestrate',
  packages=find_packages(exclude=['tests*']),
  package_data={
    '': ['*.ms', '*.yml'],
  },
  python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*',
  install_requires=install_requires,
  extras_require={
    'dev': [
      'awscli==1.15.38',
      'flake8==3.5.0',
      'mock==2.0.0',
      'nose==1.3.7',
      'numpy==1.15.0',
      'pylint==1.9.1',
      'pytest==3.6.1',
      'setuptools==40.0.0',
    ],
  },
  scripts=[
    'bin/sigopt',
  ],
  cmdclass={
    'develop': PostDevelopCommand,
    'install': PostInstallCommand,
  },
  license="Apache License 2.0",
  classifiers=(
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development',
  ),
)
