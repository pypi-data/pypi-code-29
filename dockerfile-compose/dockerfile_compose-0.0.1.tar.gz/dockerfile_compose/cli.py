#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from os.path import abspath
from shutil import copyfile

from .dockerfile_compose import build_dockerfile


def main():
    parser = ArgumentParser(description='Build a Dockerfile from a template.')
    parser.add_argument('template_file', type=str, help='template file path')
    parser.add_argument('-o', type=str, dest='out_file', default='-',
                        help='output file path. use `-` for stdout (default)')

    args = parser.parse_args()

    with open(abspath(args.template_file), 'r') as template:
        if args.out_file == '-':
            build_dockerfile(template)
            exit(0)

        out_file_arg = abspath(args.out_file)
        swap_file = open(f'{out_file_arg}.swp', 'w+')
        try:
            build_dockerfile(template, swap_file)
            swap_file.close()
            copyfile(swap_file.name, out_file_arg)
        finally:
            swap_file.close()
            os.remove(swap_file.name)
