import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daily_report",
    version="2.5",
    author="Albert Font",
    author_email="albertf80@gmail.com",
    description="A package for the production of daily and cumulative reports attached to PyBpod tasks.",
    packages=['daily_report', 'daily_report.reports'],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/AFont33/daily_reports/",
    include_package_data=True
    )
