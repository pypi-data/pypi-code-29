from setuptools import setup, find_packages

setup(
    name             = 'py-pedersen-commitment',
    version          = '1.0',
    description      = 'pedersen Commitment[Ped92]',
    author           = 'uct',
    author_email     = 'ssuminpark.1119@gmail.com',
    url = 'https://github.com/ssuminpark/seminar',
    install_requires = ['pycrypto' ],
    keywords         = ['crypto', 'pederson'],
    python_requires  = '>=2.7',
    packages=['src'],
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)