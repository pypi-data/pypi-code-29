import json
import os
import sys
from argparse import ArgumentParser
from io import BytesIO
from typing import Set
from urllib.error import HTTPError
from urllib.request import urlopen

github_url = "https://raw.githubusercontent.com/github/gitignore/master"
github_api_url = "https://api.github.com/repos/github/gitignore/contents/"


def parse_langs_from_json(resp: bytes) -> Set[str]:
    languages: Set[str] = set()
    for row in json.loads(resp):
        lang, extension = os.path.splitext(row["name"])
        if extension == ".gitignore":
            languages.add(lang)
    return languages


def get_avilable_languages() -> Set[str]:
    resp = urlopen(github_api_url)
    return parse_langs_from_json(resp.read())


def get_ignore_file(lang: str) -> bytes:
    with urlopen(f"{github_url}/{lang}.gitignore") as resp:
        contents = resp.read()
        if contents.endswith(b".gitignore"):
            fname, _ = os.path.splitext(contents.decode())
            return get_ignore_file(fname)
        else:
            return contents


def main():

    parser = ArgumentParser()
    parser.add_argument("languages", nargs="*")
    parser.add_argument("--preview", "-p", action="store_true")
    parser.add_argument("--out", "-o", default=".gitignore")
    parser.add_argument("--list", "-l", action="store_true")

    args = parser.parse_args()

    if args.list:
        for lang in get_avilable_languages():
            print(lang)
        sys.exit()

    if not args.languages:
        sys.exit("No language arguments provided (see --help)")

    out_stream: bytes = BytesIO()

    for lang in args.languages:
        try:
            resp = get_ignore_file(lang.title())
        except HTTPError as error:
            sys.exit(f"{error} (use --list to see available options)")
        else:
            out_stream.write(resp)

    with open(args.out, "wb") as out:
        contents = out_stream.getvalue()
        out.write(contents)
        if args.preview:
            print(contents.decode())
            response = input("Keep? [Y/n]: ")
            if response.lower() != "y":
                os.remove(out.name)
                sys.exit()

    print("Written to: {}".format(args.out))


if __name__ == "__main__":
    main()
