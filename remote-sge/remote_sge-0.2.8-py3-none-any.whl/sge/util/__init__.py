from os.path import abspath, join, dirname
def package_root():
    "returns the absolute path of the directory containing this package."
    return abspath(join(abspath(dirname(__file__)), '..', '..'))
