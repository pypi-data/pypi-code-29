import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

requirements = ['nbformat', 'IPython']

# setup_requirements = ['', ]

# test_requirements = ['pytest', ]

setuptools.setup(
    name='py2jnb',
    author="M.Jones, forked from Siu Kwan Lam",
    author_email='jones.0bj3@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="Utility to turn IPython scripts into Jupyter Notebook format. Forked from py2nb project.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type='text/markdown',
    # include_package_data=True,
    # keywords='oceandb-elasticsearch-driver',
    packages=setuptools.find_packages(),
    # setup_requires=setup_requirements,
    # test_suite='tests',
    # tests_require=test_requirements,
    url='https://github.com/MarcusJones/py2jnb',
    version='0.0.5',
    # zip_safe=False,
)
