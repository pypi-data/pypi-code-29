import argparse
import json
from enscramble import encode, decode, map_to_inline


parser = argparse.ArgumentParser()
parser.add_argument('--encode', required=False)
parser.add_argument('--decode', required=False)
parser.add_argument('--delimeter', required=False)
parser.add_argument('--map', required=False)
args = parser.parse_args()


def run():
    if args.encode:
        encoded, delimeter, _map = encode(args.encode)
        print(json.dumps({
            'encoded': encoded,
            'delimeter': delimeter,
            'map': map_to_inline(_map)
        }, indent=4, sort_keys=True))
    elif args.decode:
        print(decode(args.decode, args.delimeter, args.map))
