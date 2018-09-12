from os import path
from setuptools import find_packages, setup

from method_override import __version__

root = path.abspath(path.dirname(__file__))
with open(path.join(root, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='django-method-override',
    version=__version__,
    description='Django Middleware for HTTP Method Override Form Params & Header',  # noqa
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='LocalMed',
    author_email='pete.browne@localmed.com',
    url='https://gitlab.com/localmed/django-method-override',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'django>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
