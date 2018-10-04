from typing import Dict, List
import json
import sys
import argparse

from .loaders import load

def key_val_to_dict(pairs: List[str]) -> Dict:
    """
    Converts KEY=VALUE pairs into a {KEY: VALUE, ...} dict
    """
    # TODO error handling
    variable_dict = {}
    for pair in pairs:
        key, value = pair.split('=', 1)
        variable_dict[key] = value
    return variable_dict


def main():

    parser = argparse.ArgumentParser(description="Configuration for Humans.")
    parser.add_argument(
        "--variable",
        "-v",
        dest='variables',
        action='append',
        help="Variables to pass to the configuration file",
    )
    parser.add_argument("filename", metavar="FILENAME", help="Configuration File")
    args = parser.parse_args()
    # TODO Optional yaml
    # TODO README
    # TODO implement timeout
    generated = load(args.filename, key_val_to_dict(args.variables))
    print(json.dumps(generated, indent=2))
