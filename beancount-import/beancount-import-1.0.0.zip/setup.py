from setuptools import setup

setup(
    name='beancount-import',
    description='Semi-automatic importing of external data into beancount.',
    url='https://github.com/jbms/beancount-import',
    version='1.0.0',
    author='Jeremy Maitin-Shepard',
    author_email="jeremy@jeremyms.com",
    license='GPLv2',
    packages=["beancount_import"],
    package_data={
        'beancount_import': ['frontend_dist/prod/index.html'],
    },
    install_requires=[
        'beancount>=2.1.2',
        'tornado',
        'numpy',
        'scipy',
        'scikit-learn',
        'nltk',
    ],
    test_requirements=[
        'pytest',
    ],
)
