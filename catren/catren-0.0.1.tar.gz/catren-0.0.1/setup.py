import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="catren",
    version="0.0.1",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Create R markdown files from markdown files and scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/nbless",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'catrmd = catren.catrmd:command_line_runner',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
