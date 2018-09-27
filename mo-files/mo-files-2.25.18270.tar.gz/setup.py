from setuptools import setup
setup(
    description="More Files! Steamlined for UTF8 and JSON.",
    license="MPL 2.0",
    author="Kyle Lahnakoski",
    author_email="kyle@lahnakoski.com",
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"],
    install_requires=["mo-dots","mo-future","mo-logs>=2.24.18269"],
    version="2.25.18270",
    url="https://github.com/klahnakoski/mo-files",
    zip_safe=False,
    packages=["mo_files"],
    long_description="More Files!\n==========\n\nThe `File` class makes the default assumption all files have cr-delimited unicode content that is UTF-8 encoded. This is great for JSON files. It also provides better OO over some common file manipulations.\n\n",
    name="mo-files"
)