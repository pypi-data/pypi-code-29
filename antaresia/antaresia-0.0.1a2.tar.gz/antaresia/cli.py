import json
import sys

from .loaders import load

def main():
    # TODO Proper parsing
    # TODO Optional yaml
    # TODO README
    filename = sys.argv[-1]
    print(json.dumps(load(filename), indent=2))
