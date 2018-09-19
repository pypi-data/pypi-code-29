from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-yournotifier',
    version='1.0.0',
    author='Ivan Lukyanets',
    author_email='lukyanets.ivan@gmail.com',
    url='https://github.com/1vank1n/django-yournotifier',
    packages=[
        'yournotifier',
    ],
    include_package_data=True,
    license='MIT',
    description='A simple integration for use yournotifier.com',
    keywords='django yournotifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests==2.19.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
)
