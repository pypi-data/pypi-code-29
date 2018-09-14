from setuptools import setup, find_packages

setup(
    name='simpl-users',
    version="0.7.2",
    description='simpl-users provides Wharton SIMPL Users',
    long_description='',
    author='Jeff Triplett',
    author_email='jeff@revsys.com',
    url='https://github.com/simplworld/simpl-users',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "django-username-email==2.1.3",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)

