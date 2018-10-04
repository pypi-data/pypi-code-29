from setuptools import setup, find_packages

setup(
    name='pppTest',
    version='1.0.0',
    description=(
        'A testing'
    ),
    long_description=open('README.rst').read(),
    author='NewBee',
    author_email='NewBee@gmail.com',
    maintainer='NewBee',
    maintainer_email='NewBee@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/NewBee',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
