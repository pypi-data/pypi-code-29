from setuptools import find_packages, setup

version = "0.1.2"

setup(
    name='pytest-fantasy',
    version=version,
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/wangwenpei/pytest-fantasy',
    download_url='https://github.com/wangwenpei/pytest-fantasy/tarball/master',
    license='MIT',
    author='WANG WENPEI',
    zip_safe=False,
    test_suite="tests",
    author_email='stormxx@1024.engineer',
    description='Pytest plugin for Flask Fantasy Framework',
    keywords='fantasy,flask',
)
