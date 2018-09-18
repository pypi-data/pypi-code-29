from setuptools import setup

setup(
    name='pyftpd-sink',
    version='0.3',
    # description='',
    author='Fabian Peter Hammerle',
    author_email='fabian@hammerle.me',
    url='https://git.hammerle.me/fphammerle/pyftpd-sink',
    license='MIT',
    keywords=[
        'ftp',
        'server',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=[],
    scripts=[
        'pyftpd-sink',
    ],
    install_requires=[
        'pyftpdlib>=1.5.4',
    ],
    tests_require=[],
)
