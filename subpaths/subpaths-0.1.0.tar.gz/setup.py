import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subpaths",
    version="0.1.0",
    author="Lawrence Weikum",
    author_email="lweikum@gmail.com",
    description="Finding common subpaths between paths.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lawrencemq/subpaths",
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)