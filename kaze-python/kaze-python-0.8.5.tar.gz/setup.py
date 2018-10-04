#!/usr/bin/env python3
"""The setup script."""

from setuptools import setup, find_packages
try:  # pip version >= 10.0
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # pip version < 10.0
    from pip.req import parse_requirements
    from pip.download import PipSession


with open('README.rst') as readme_file:
    readme = readme_file.read()

# get the requirements from requirements.txt
install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='kaze-python',
    python_requires='>=3.6',
    version='0.8.5',
    description="Python Node and SDK for the kaze blockchain",
    long_description=readme,
    author="Moe Sayadi",
    author_email='Moe@KAZEBLOCKCHAIN.ch',
    maintainer="Ela soltani",
    maintainer_email='ela@KAZEBLOCKCHAIN.ch',
    url='https://github.com/KAZEBLOCKCHAIN/kaze-python',
    packages=find_packages(include=['kaze']),
    entry_points = {
        'console_scripts': [
            'np-prompt=kaze.bin.prompt:main',
            'np-api-server=kaze.bin.api_server:main',
            'np-bootstrap=kaze.bin.bootstrap:main',
            'np-reencrypt-wallet=kaze.bin.reencrypt_wallet:main',
            'np-sign=kaze.bin.sign_message:main',
            'np-export=kaze.bin.export_blocks:main',
            'np-import=kaze.bin.import_blocks:main',
        ],
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='kaze, python, node',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
