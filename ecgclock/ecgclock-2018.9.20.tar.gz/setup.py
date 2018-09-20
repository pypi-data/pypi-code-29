from setuptools import setup, find_packages

setup(
    name='ecgclock',
    version='2018.09.20',
    description='ECG clock plotter',
    url='https://bitbucket.org/atpage/ecgclock/',
    author='Alex Page',
    author_email='alex.page@rochester.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0',
    keywords='Holter ECG EKG clock QT LQTS',
    packages=find_packages(exclude=['tests']),
    install_requires=['matplotlib', 'numpy', 'python-dateutil', 'cycler', 'pandas'],
    entry_points={
        'console_scripts': [
            'make_qtclock=ecgclock.qtclock:main',
        ],
    },
    package_data={
        'ecgclock': ['example_data/*.csv'],
        # TODO: normal range examples
    },
)
