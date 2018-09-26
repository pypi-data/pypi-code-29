import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbot-manager",
    version="0.0.3",
    author="ovsoil",
    author_email="huaxin.yu@atmatrix.org",
    description="Develop tools for ATN DBot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ATNIO/dbot-manager",
    packages=setuptools.find_packages(),
    install_requires=[
        'click==6.7',
        'eth_utils==1.2.2',
        'eth_keyfile==0.5.1',
        'typing==3.6.6',
        'eth_account==0.3.0',
        'web3==4.7.2',
        'requests==2.19.1'
    ],
    package_data={
        '': ['contracts.json']
    },
    scripts=[
        'dbot-service'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
