import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polish_genbank",
    version="0.0.1",
    author='Guanliang Meng',
    author_email='mengguanliang@genomics.cn',
    description="To check for the internal stop codon in Genbank or FASTA file (CDS), then substitute the internal stop codon with NNN.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.4',
    url='https://github.com/linzhi2013/polish_genbank',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['biopython'],

    entry_points={
        'console_scripts': [
            'polish_genbank=polish_genbank.polish_genbank:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)