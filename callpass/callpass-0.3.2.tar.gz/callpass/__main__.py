from argparse import ArgumentParser

from . import Callpass, ValidatedCallpass


def arguments():
    parser = ArgumentParser(prog="callpass", description="Generate an APRS-IS passcode")
    parser.add_argument(
        "callsign", nargs="+", help="The callsign you want an APRS-IS code for"
    )
    parser.add_argument(
        "-v",
        "--validate",
        action="store_true",
        help="USA-only validation of callsign format, existence, and expiry",
    )
    return parser.parse_args()


def main():
    args = arguments()

    if args.validate:
        _Callpass = ValidatedCallpass
    else:
        _Callpass = Callpass

    for callsign in args.callsign:
        print(_Callpass(callsign))


if __name__ == "__main__":
    main()
