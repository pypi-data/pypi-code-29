from setuptools import setup


setup(
    name='pypigit-version',
    version='0.1.5',
    url='https://github.com/anthill-utils/pypigit-version',
    author='desertkun',
    author_email='desertkun@gmail.com',
    description='Automatically set package version from Git.',
    license='http://opensource.org/licenses/MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'Programming Language :: Python'
    ],
    zip_safe=False,
    py_modules=['pypigit_version'],
    install_requires=[
        'setuptools >= 8.0'
    ],
    entry_points="""
        [distutils.setup_keywords]
        git_version = pypigit_version:git_version
    """,
)