from setuptools import setup

setup(
    name="Grank",
    version="0.0.1",
    py_modules=['grank'],
    install_requires= [
        'Click',
        'Pandas',
        'Numpy',
        'Matplotlib',
        'Requests'
    ],
    entry_points="""
        [console_scripts]
        grank=grank:cli
    """
)