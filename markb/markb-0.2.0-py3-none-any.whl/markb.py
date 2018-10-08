#!/usr/bin/env python3
# markb
# Get a markdown file via argument and output to a tempfile.
# Open automatically with browser. Fun!

from argparse import ArgumentParser
from markdown import markdown
from tempfile import NamedTemporaryFile
import webbrowser


def main():
    description = """Render markdown files to
    a temporary file and open it in a browser (YOUR browser!)"""
    parser = ArgumentParser(description=description)
    parser.add_argument("filename",
                        help="A markdown file",
                        default="README.md",
                        nargs="?")
    args = parser.parse_args()

    try:
        with open(args.filename) as md:
            html = markdown(md.read())

        tempfile = NamedTemporaryFile(mode="w+", delete=False, suffix=".html")
        tempfile.write(html)
        webbrowser.open("file://{}".format(tempfile.name))

    except FileNotFoundError:
        print('File not found "{filename}"'.format(filename=args.filename))


if __name__ == "__main__":
    main()
