import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tests
suite = tests.suite

if __name__ == '__main__':
    tests.main()
