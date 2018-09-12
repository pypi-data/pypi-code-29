#!/user/bin/env python

from setuptools import setup, find_packages

DEPENDENCIES = [
    'boto3>=1.7.57',
    'lambda-uploader>=1.3.0',
    'jinja2>=2.10',
]

STYLE_REQUIRES = [
    'flake8>=3.5.0',
    'pylint>=1.9.2',
]

TEST_REQUIRES = []

EXTRAS_REQUIRE = {
    'test': TEST_REQUIRES,
    'style': STYLE_REQUIRES,
    'lint': STYLE_REQUIRES,
    'test-requirements': TEST_REQUIRES + STYLE_REQUIRES,
}

setup(
    name='aws-lambda-pypackager',
    description='Opinionated packaging helper for Python AWS Lambda Projects.',
    keywords='aws lambda serverless',
    version='0.1.0',
    install_requires=DEPENDENCIES,
    tests_require=TEST_REQUIRES + STYLE_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    author='Jim Rosser',
    maintainer_email="jarosser06@gmail.com",
    url="https://github.com/jarosser06/aws-lambda-pypackager",
    entry_points={
        'console_scripts': [
            'pypackager=pypackager.shell:main'
        ]
    },
)
