from setuptools import find_packages, setup
from setuptools.command.install import install
from subprocess import check_call

with open("README.rst", "r") as fh:
    long_description = fh.read()


class Install(install):
    def run(self):
        check_call('ls')
        install.run(self)


setup(
    name='libmediainfo_cffi',
    version='1.0.2',
    author='Alessandro Cerruti',
    author_email='thereap3r97@gmail.com',
    description='CFFI interface for libmediainfo',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/strychnide/libmediainfo_cffi',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/strychnide/libmediainfo_cffi',
        'Issues': 'https://github.com/strychnide/libmediainfo_cffi/issues'
    },
    python_requires='>=3.5',
    setup_requires=['cffi'],
    cffi_modules=['libmediainfo_cffi/_cffi.py:ffi'],
    install_requires=[
        'cffi'
    ],
    extras_require={
        'dev': [
            'flake8',
            'flake8-sorted-keys',
            'flake8-import-order',
            'flake8-quotes',
            'flake8-bugbear',
        ]
    },
    packages=find_packages(exclude=['*_cffi.py']),
    # ext_package='libmediainfo_cffi',
    cmdclass={
        'install': Install,
    },
)

