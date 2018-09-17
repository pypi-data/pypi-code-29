from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="xl-sudoku-solver",
    version="0.0.1.post3",
    packages=['xl_sudoku_solver'],
    entry_points={
        "console_scripts": [
            "xl-sudoku-solver = xl_sudoku_solver.__main__:main"
        ]
    },
    include_package_data=True,
    test_suite="tests",

    author="Xulun Li",
    author_email="lixulun99@hotmail.com",
    description="A beautiful Sudoku solver",
    license="MIT",
    url="https://github.com/lixulun/XL-Sudoku-Solver",
    long_description=long_description,
    long_description_content_type="text/markdown"
)