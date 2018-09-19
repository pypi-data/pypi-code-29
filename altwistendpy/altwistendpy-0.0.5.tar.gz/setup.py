import setuptools

import versioneer


with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='altwistendpy',
    description="Extras for working with Twisted.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/altwistendpy',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'amp = altwistendpy.examples.amp.cli:cli',
        ],
    },
    install_requires=[
        'attrs',
        'click',
        'gitignoreio',
        'twine',
        'twisted',
        'wheel',
    ],
)
