try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

setup(
        name="sasrunner",
        version='0.0.2',
        description="SAS runner",
        author="Joe Dougherty",
        author_email="josepd@wharton.upenn.edu",
        url="https://wrds-web.wharton.upenn.edu/wrds/",
        packages=['sasrunner'],
        keywords = ['SAS', 'etl'],
        )

