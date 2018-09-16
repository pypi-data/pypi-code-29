import sys
from os.path import abspath, dirname, join, relpath, basename
from typing import TextIO


def include_dockerfile(dockerfile: TextIO, out: TextIO):
        content_start = False
        for line in dockerfile:
            # strip directives we don't like
            if line.lower().startswith(('#', 'from', 'cmd')):
                continue
            # trim beginning whitespace
            if not content_start and not line.strip():
                continue
            content_start = True
            out.write(line)


def build_dockerfile(template_file: TextIO, out_file: TextIO = None):
    if out_file:
        out_dest = out_file
        friendly_template_path = relpath(template_file.name, dirname(out_file.name))
    else:
        out_dest = sys.stdout
        friendly_template_path = basename(template_file.name)

    def out(x):
        print(x, file=out_dest)

    out('''
#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "dockerfile-compose"
#
# PLEASE DO NOT EDIT IT DIRECTLY. EDIT "{}" INSTEAD
#
    '''.strip().format(friendly_template_path))
    for line in template_file:
        if line.startswith('# @include'):
            include_file_arg = line.split()[2].strip()
            if not include_file_arg:
                continue

            include_file = abspath(join(dirname(template_file.name), include_file_arg))

            if out_file:
                include_file_rel = relpath(include_file, dirname(out_file.name))
            else:
                include_file_rel = include_file_arg
            out(line.replace(include_file_arg, include_file_rel).strip())

            with open(abspath(include_file)) as df:
                include_dockerfile(df, out_dest)
            out(f'# @endinclude {include_file_rel}')

            continue
        out(line.strip())
