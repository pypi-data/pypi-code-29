#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import find
from public import public

# path/to/repo/.../<section_name>.md
# path/to/repo/.../<section_name2>.md


def _has_header(body):
    return body.lstrip()[0] == "#"


HEADERS = dict(
    badges="",
    description="",
    how="How it works"
)


def _active_sections(self):
    result = []
    for name in self.ordering:
        if name not in self.disabled:
            result.append(name)
    return result


def _get_sections(self):
    result = []
    for name in _active_sections(self):
        body = str(getattr(self, name, ""))
        if body:
            result.append([name, body])
    return result


@public
class Readme:
    ordering = ["badges", "description", "install", "features", "requirements", "usage", "config", "how", "examples", "todo", "links"]
    disabled = []
    headers = None
    header_lvl = 3

    def __init__(self, path, **kwargs):
        self.load(path)
        self.update(**kwargs)
        self.headers = HEADERS

    def update(self, *args, **kwargs):
        inputdict = dict(*args, **kwargs)
        for k, v in inputdict.items():
            setattr(self, k, v)

    def header(self, section):
        header = self.headers.get(section, section.title())
        if not header:  # without header
            return ""
        if "#" in header:  # custom headering level
            return header
        return "%s %s" % ("#" * self.header_lvl, header)  # default headering level

    def render(self):
        sections = []
        for name, body in _get_sections(self):
            # todo: clean
            if not _has_header(body):  # without header
                header = self.header(name)
                body = "%s\n%s" % (header, str(body).lstrip())
            sections.append(str(body).lstrip().rstrip())
        return "\n\n".join(filter(None, sections))

    def save(self, path):
        output = self.render()
        if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        open(path, "w").write(output)

    def load_file(self, path):
        content = open(path).read()
        name, ext = os.path.splitext(os.path.basename(path))
        setattr(self, name, content)

    def load(self, path="."):
        if not path:
            path = os.getcwd()
        self.files = list(find.files(path, followlinks=True))
        for f in self.files:
            name, ext = os.path.splitext(os.path.basename(f))
            if ext == ".md":
                self.load_file(f)


USAGE = 'usage: python -m %s' % __file__.split("/")[-1].split(".")[0]


def _cli():
    print(Readme().render())


if __name__ == '__main__':
    if sys.argv[-1] == "--help":
        print(USAGE)
        sys.exit(0)
    _cli()
