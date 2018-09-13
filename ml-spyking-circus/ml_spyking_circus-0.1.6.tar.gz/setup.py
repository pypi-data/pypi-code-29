import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

pkgs = setuptools.find_packages()
print('found these packages:', pkgs)

pkg_name='ml_spyking_circus'

setuptools.setup(
    name=pkg_name,
    version="0.1.6",
    author="Jeremy Magland",
    author_email="",
    description="MountainLab wrapper for spyking circus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magland/ml_spyking_circus",
    packages=pkgs,
    package_data={
        # Include all processor files
        '': ['*.mp']
    },
    install_requires=
    [
        'numpy',
        'mlprocessors',
	'mountainlab_pytools',
        'numpydoc',
        'h5py'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    conda={
        "build_number":0,
        "build_script":[
            "python -m pip install --no-deps --ignore-installed .",
            "CMD=\"ln -sf $SP_DIR/"+pkg_name+" `CONDA_PREFIX=$PREFIX ml-config package_directory`/"+pkg_name+"\"",
            "echo $CMD",
            "$CMD"
        ],
        "test_commands":[
            "ml-list-processors",
            "ml-spec spyking_circus.sort"
        ],
        "test_imports":[
        ],
        "requirements":[
            "python",
            "pip",
            "mountainlab",
            "mlprocessors",
            "mountainlab_pytools",
            "numpy",
            "numpydoc",
            "h5py"
        ]
    }
)
