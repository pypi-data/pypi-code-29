import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

pkgs = setuptools.find_packages()
print('found these packages:', pkgs)

pkg_name='ml_mearec'

setuptools.setup(
    name=pkg_name,
    version="0.1.6",
    author="Jeremy Magland",
    author_email="",
    description="MountainLab wrapper for MEArec",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magland/ml_mearec",
    packages=pkgs,
    package_data={
        # Include all processor files
        '': ['*.mp']
    },
    install_requires=
    [
	'MEAutility',
        'h5py',
        'numpy',
        'click',
        'neo',
        'elephant',
        'matplotlib',
        'scipy',
        'quantities',
        'pyyaml',
        'numpy',
        'mlprocessors',
        'mountainlab_pytools',
        'prompt_toolkit'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    conda={
        "build_number":0,
        "build_script":[
            #"python -m pip install --no-deps --ignore-installed .",
            "python -m pip install .",
            "CMD=\"ln -sf $SP_DIR/"+pkg_name+" `CONDA_PREFIX=$PREFIX ml-config package_directory`/"+pkg_name+"\"",
            "echo $CMD",
            "$CMD"
        ],
        "test_commands":[
            "ml-list-processors",
            "ml-spec -p mearec.gen_spiketrains",
            "ml-spec -p mearec.gen_recording"
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
            "h5py"
        ]
    }
)
