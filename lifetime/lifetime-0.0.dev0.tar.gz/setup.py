import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name='lifetime',
    version='0.0dev',
    author="reehc",
    description="Measure my day",
    long_description=long_description,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'lifetime = lifetime.me:main',
        ],
    },
)
