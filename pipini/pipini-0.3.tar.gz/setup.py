from setuptools import setup

setup(
    name="pipini",
    version="0.3",
    platforms='Windows',
    py_modules=["pipini"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        pipini=pipini:cli
    '''
)
