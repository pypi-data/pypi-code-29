#!/usr/bin/env python3
import os
import sys
import json
import base64
import hashlib
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--wheel-hashes', action='store_true')
    args = parser.parse_args()
    if args.wheel_hashes:
        # First find all of wheels and their names
        if not os.path.exists("./localwheels/"):
            print("Missing localwheels directory.")
            sys.exit(3)
        files = os.listdir("./localwheels/")
        for filename in files:
            fullpath = os.path.join("./localwheels/", filename)
            with open(fullpath, "br") as fobj:
                data = fobj.read()

            # Now compute the hash
            digest = hashlib.sha256(data).hexdigest()
            print("{} --hash=sha256:{}".format(fullpath, digest))


    else:
        # Find the Pipfile.lock and create a requirements-build.txt with all hashes
        if not os.path.exists("Pipfile.lock"):
            print("Pipfile.lock file is missing in the current directory.")
            sys.exit(1)
        with open("Pipfile.lock") as fobj:
            data = json.load(fobj)

        defaults = data["default"]
        for name in defaults:
            package_name = "{}{}".format(name, defaults[name]["version"])
            hashes = " ".join(["--hash={}".format(value) for value in defaults[name]["hashes"]])
            print("{} {}".format(package_name,hashes))
                


if __name__ == "__main__":
    main()