from setuptools import setup, find_packages


setup(
    name="pypi-chat-server",
    version='0.0.2',
    description="A alfa project of PyQT chat.",
    long_description="A chat project on python 3 and PyQt5",
    author="Daniyar Kaliyev",
    author_email="danikspirit@gmail.com",
    url="https://github.com/dankaliyev/pypi-chat-server",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['PyQT5 chat server', 'chat PyQt 5', 'server jim chat'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        "SQLAlchemy==1.1.14",
    ],
    extras_require={
        'dev': ['flake8==3.4.1',],
        'test': ["pytest==3.2.2",
                 "pytest-cov==2.5.1",
                 "pytest-sugar==0.9.0",
                 "PyYAML==3.12",],
    },
    entry_points={
         'console_scripts': [
            'pypi-chat-server=pypi_server.main:main',
        ],
    },
)