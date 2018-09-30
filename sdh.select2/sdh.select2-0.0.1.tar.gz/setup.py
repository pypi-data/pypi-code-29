from setuptools import find_packages, setup

version = '0.0.1'

needed = [
    'Django>=1.11.0',
    'djangorestframework>=3.8.0'
]


setup(
    name='sdh.select2',
    version=version,
    url='https://sdh.com.ua/',
    author='Software Development Hub LLC',
    author_email='dev-tools@sdh.com.ua',
    description='Select2 API endpoints',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['sdh'],
    eager_resources=['sdh'],
    include_package_data=True,
    entry_points={},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

