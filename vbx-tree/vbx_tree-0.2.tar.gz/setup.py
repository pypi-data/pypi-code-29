import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='vbx_tree',
    version='0.2',
    description='Fast project tree creator',
    license="MIT",
    long_description=long_description,
    author='vbxx3',
    author_email='vbabrouski@outlook.com',
    url="https://www.linkedin.com/in/vbxx3",
    packages=setuptools.find_packages(),  #same as name
    install_requires=["setuptools", "wheel"], #external packages as dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
