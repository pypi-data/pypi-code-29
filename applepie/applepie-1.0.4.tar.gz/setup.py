from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='applepie',
    author='Jordan Ambra',
    author_email='jordan@boom.app',
    url='https://github.com/boomletsgo/applepie',
    version='1.0.4',
    classifiers=classifiers,
    description='Apple Pay library',
    keywords='Apple Pay',
    packages=["applepie"],
    install_requires=[
        "cryptography>=2.0.0",
        "py-moneyed>=0.7.0",
        "pyOpenSSL>=18.0.0",
        "six>=1.0.0"
    ],
    include_package_data=True,
    license='The Unlicense',
)
