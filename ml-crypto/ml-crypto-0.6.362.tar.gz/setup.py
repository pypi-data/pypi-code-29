import setuptools
import os

build = os.environ.get('PIP_BUILD', '0-internal')
keywords = os.environ.get('PIP_KEYWORDS', 'test')

with open("README.md", "r") as fh:
    long_description = fh.read().strip()

if len(str(build).split('.')) > 1:
    version = build
else:
    with open("version.txt", "r") as fh:
        file_version = fh.read().strip()

    version = '{}.{}'.format(file_version, build)

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().strip().split('\n')

setuptools.setup(
    name="ml-crypto",
    version=version,
    author="MissingLink.ai",
    author_email="support@missinglink.ai",
    description="pyCrypto wrapper, used by various MissingLink.ai libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://missinglink.ai",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7'
    ),
    package_data={
        '': ['*.txt', '*.rst', '*.MD', '*.md'],
    },
    py_modules=['missinglink.crypto'],
    extras_require={
        'pycrypto': ["pycrypto~=2.6.1"],
        'pycryptodomex': ["pycryptodome~=3.6.4"]
    },
    install_requires=install_requires
)
