from setuptools import setup, find_packages


setup(
    name="pypi-chat",
    version='0.0.4',
    description="A project of pypi chat.",
    long_description="A chat-client project on python 3 and PyQt5",
    author="Daniyar Kaliyev",
    author_email="danikspirit@gmail.com",
    url="https://github.com/dankaliyev/pypi_chat-cli",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['PyQT5 chat client', 'chat PyQt 5', 'client jim chat'],
    packages=find_packages('src'),
    package_dir={'pypi_client': 'src/pypi_client'},
    package_data={'pypi_client':
                        ['ui/img/*.png',
                         'ui/img/*.jpg',
                         'ui/img/*.gif']
    },
    install_requires=[
        "Pillow==4.3.0",
        "PyQt5==5.9",
        "SQLAlchemy==1.1.14",
    ],
    extras_require={
        'dev': ['flake8==3.4.1'],
        'test': ["pytest==3.2.2",
                 "pytest-cov==2.5.1",
                 "pytest-sugar==0.9.0",
                 "PyYAML==3.12"],
    },
    entry_points={
        'gui_scripts': [
            'pypi-chat= pypi_client.main:main',
        ],
    },
)