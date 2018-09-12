from setuptools import setup
import versioneer


if __name__ == "__main__":
    setup(
        name='fs-gcsfs',
        author="Othoz",
        description="A PyFilesystem interface to Google Cloud Storage",
        url="http://othoz.com",  # TODO
        license="MIT",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        install_requires=[
            "fs~=2.1.0"
        ],
        entry_points={
            'fs.opener': [
                'gs = gcsfs.opener:GCSFSOpener',
            ]
        },
        packages=["gcsfs"],
        # Missing: python_requires
    )
