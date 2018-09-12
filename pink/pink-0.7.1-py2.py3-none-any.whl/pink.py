#!/usr/bin/env python
# coding=utf-8

import argparse
import contextlib
import os
import sys

import black
import delegator
import glob2
from isort import SortImports

PEP8_MAXLINE = 79
VERSION = "0.7.1"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description="Format code via command line with `black` and `isort`"
    )
    parser.add_argument(
        "paths",
        metavar="PATHS",
        type=str,
        nargs="*",
        help="Files and directories that should be executed format command.",
    )
    parser.add_argument(
        "-l",
        "--line",
        type=int,
        default=PEP8_MAXLINE,
        help="`black` How many character per line to allow.[default: 79]",
    )
    parser.add_argument(
        "-sp",
        "--settings_path",
        type=str,
        default="",
        help="`isort` Explicitly set the settings path instead of auto "
        "determining based on file location",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Displays the current version of pink",
    )
    return parser


@contextlib.contextmanager
def mute_stdout():
    """
    屏蔽输出
    """
    tmp_stdout = sys.stdout
    sys.stdout = None
    try:
        yield
    except Exception:
        pass
    sys.stdout = tmp_stdout


def command_line_runner():
    """
    主函数
    """
    python = sys.executable
    black_exec = black.__file__.rstrip("cdo")

    parser = get_parser()
    args = vars(parser.parse_args())
    if args["version"]:
        print(VERSION)
        return

    paths = args["paths"]
    if not paths:
        parser.print_help()
        return

    settings = args["settings_path"]
    isort_setting_path = os.path.abspath(settings) if settings else None
    maxline = args["line"]

    cnt = 0
    print("🎉✨  Formatting code...")
    for path in paths:
        for file in glob2.glob(path):
            cnt += 1
            with mute_stdout():
                SortImports(file, settings_path=isort_setting_path)
        # 写在同一循环内 black 操作执行有误
        for file in glob2.glob(path):
            delegator.run(
                f"{python} {black_exec} {file} --line-length {maxline}"
            )
    print("✨🎉  All {} files done!".format(cnt))
    sys.exit()


if __name__ == "__main__":
    command_line_runner()
