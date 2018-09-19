from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = None


setup(
    name = 'pinwheel',
    packages = ['pinwheel'],
    version = '0.0.0',
    description = 'A testing framework for Airflow and Hive queries.',
    long_description = long_description,
    author = 'Adrian Kuhn',
    author_email = 'adrian.kuhn@airbnb.com',
    url = 'https://github.com/akuhn/pinwheel',
)
