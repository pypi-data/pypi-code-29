import sys
import argparse
import string
from . import encode, decode


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(command=None)
    sub_parser = parser.add_subparsers(help="sub commands")

    cmd = "encode"
    command1 = sub_parser.add_parser(cmd, help=cmd)
    command1.set_defaults(command=cmd)
    command1.add_argument("input", type=int, help="the number to encode")
    command1.add_argument(
        "--left", default=string.ascii_uppercase, help="left text base"
    )
    command1.add_argument("--right", default=string.digits, help="right text base")
    command1.add_argument(
        "--left-digit", type=int, default=4, help="the length of left part"
    )
    command1.add_argument(
        "--right-digit", type=int, default=4, help="the length of right part"
    )

    cmd = "decode"
    command1 = sub_parser.add_parser(cmd, help=cmd)
    command1.set_defaults(command=cmd)
    command1.add_argument("input", help="the text to decode")
    command1.add_argument(
        "--left", default=string.ascii_uppercase, help="left text base"
    )
    command1.add_argument("--right", default=string.digits, help="right text base")
    command1.add_argument(
        "--left-digit", type=int, default=4, help="the length of left part"
    )
    command1.add_argument(
        "--right-digit", type=int, default=4, help="the length of right part"
    )

    args = parser.parse_args()
    command = args.command

    commands = {"encode": encode, "decode": decode}

    try:
        r = commands[command](
            args.input, args.left, args.right, args.left_digit, args.right_digit
        )
        print(r)
    except Exception as e:
        print(e)
        sys.exit(1)
