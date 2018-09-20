import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dataf",
    version="0.0.3",
    author="Boumendil Benjamin",
    author_email="benjamin.boumendil@gmail.com",
    description="Create project to manipulate data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenjaminBoumendil/dataf",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.5',
    install_requires=[
        'SQLAlchemy', 'PyYAML', 'slackclient', 'flask', 'flasgger',
        'docutils', 'mako', 'alembic'
    ],
    entry_points={
        'console_scripts': ['dataf=dataf.command_line:main']
    },
    include_package_data=True,
)
