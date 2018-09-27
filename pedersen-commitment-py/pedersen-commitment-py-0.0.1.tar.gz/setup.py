from setuptools import setup, find_packages

setup(
    name             = 'pedersen-commitment-py',
    version          = '0.0.1',
    description      = 'pedersen Commitment[Ped92]',
    author           = 'uct',
    author_email     = 'ssuminpark.1119@gmail.com',
    url = 'https://github.com/ssuminpark/seminar',
    install_requires = ['pycrypto' ],
    long_description=open('README.md').read(),
    keywords         = ['crypto', 'pederson'],
    python_requires  = '>=2.7',
    packages=['Pedersen'],
    py_modules=['pedersen'],
    classifiers      = [
       "Programming Language :: Python :: 3"
    ]
)
