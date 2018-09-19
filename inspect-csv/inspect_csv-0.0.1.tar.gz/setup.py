from setuptools import setup

setup(
    name="inspect_csv",
    version="0.0.1",
    author="Nicholas Del Grosso",
    author_email="delgrosso.nick@gmail.com",
    description="some simple CSV tools for summarizing tabular data.",
    #url="https://github.com/pypa/sampleproject",
    py_modules=['chist'],
    install_requires=['click', 'matplotlib', 'pandas'],
    entry_points="""
        [console_scripts]
        hist=chist:hist
        hist2=chist:hist2
        showcsv=chist:show
    """,
)
