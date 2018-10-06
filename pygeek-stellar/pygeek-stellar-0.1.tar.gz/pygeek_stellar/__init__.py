# Local imports
from .geek_stellar_cmd import GeekStellarCmd
from .cli_session import *


def main():
    print_banner()

    session = cli_session_init()
    if not session:
        return

    cmd = GeekStellarCmd(session)
    cmd.do_cls(None)
    print_current_session_account(session)
    cmd.do_help(None)
    cmd.cmdloop()


def print_banner():
    ch = '#'
    length = len(CLI_BANNER_TEXT) + 8
    spaced_text = ' %s ' % CLI_BANNER_TEXT
    banner = spaced_text.center(length, ch)
    print('\n' + ch * length)
    print(banner)
    print(ch * length + '\n')


def print_current_session_account(session):
    print('\nThe following account was chosen: {}\n'.format(session.to_str()))


if __name__ == "__main__":
    main()
