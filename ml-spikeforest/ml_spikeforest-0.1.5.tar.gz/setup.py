import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

pkgs = setuptools.find_packages()
print('found these packages:', pkgs)

pkg_name='ml_spikeforest'

setuptools.setup(
    name=pkg_name,
    version="0.1.5",
    author="Jeremy Magland",
    author_email="",
    description="MountainLab package with spike sorting utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magland/ml_spikeforest",
    packages=pkgs,
    package_data={
        # Include all processor files
        '': ['*.mp']
    },
    install_requires=
    [
        'numpy',
        'mountainlab_pytools',
        'mlprocessors',
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
            "ml-spec spikeforest.create_timeseries_hdf5"
        ],
        "test_imports":[
            "ml_spikeforest"
        ],
        "requirements":[
            "python",
            "mountainlab",
            "mountainlab_pytools",
            "mlprocessors",
            "numpy",
            "h5py"
        ]
    }
)
