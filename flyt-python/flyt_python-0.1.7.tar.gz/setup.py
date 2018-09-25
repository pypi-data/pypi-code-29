import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = ["redis", "websocket-client==0.50.0", "requests"]


setuptools.setup(
    name="flyt_python",
    version="0.1.7",
    author="ayush_98",
    author_email="ayush@flytbase.com",
    description="Python package for Drone Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='LICENSE.txt',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        #"License :: ,
        "Operating System :: OS Independent",
    ],
)
