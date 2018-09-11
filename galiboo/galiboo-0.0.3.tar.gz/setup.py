import setuptools


setuptools.setup(
    name="galiboo",
    version="0.0.3",
    url="https://github.com/galiboo/galiboo-python",
    author="Subhash",
    author_email="subby@galiboo.com",
    description="The official Python SDK for Galiboo's Music API.",
    long_description=open('README.md').read(),
    packages=["galiboo"],
    test_suite='tests',
    tests_require=["pytest", "responses"],
    install_requires=["requests"],
    #setup_requires=["pytest-runner"],
)
