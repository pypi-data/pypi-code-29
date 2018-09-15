#!/usr/bin/env python3.6
import sys

from typing import List
from colorama import init, Fore, Style
import consolemd

from nts import __version__
from nts.ui.create import create_note
from nts.ui.delete import delete_note
from nts.ui.edit import edit_note
from nts.ui.search import search_notes
from nts.fstring import f

import nts.api as nts


helptext = f("""{Style.BRIGHT}note to self {__version__}

{Style.BRIGHT}USAGE:
    {sys.argv[0]}{Style.NORMAL} creates new note{Style.BRIGHT}
    {sys.argv[0]}{Style.NORMAL} {Fore.BLUE}[note] {Fore.RESET}displays note{Style.BRIGHT}
    {sys.argv[0]}{Style.NORMAL} {Fore.BLUE}[operation] {Fore.CYAN}[args]
{Fore.RESET}
{Style.BRIGHT}OPERATIONS:{Style.NORMAL}
    {Fore.RED}-h            {Fore.RESET}shows help
    {Fore.RED}-d {Fore.BLUE}note title {Fore.RESET}deletes note
    {Fore.RED}-e {Fore.BLUE}note tltle {Fore.RESET}edits note
    {Fore.RED}-s {Fore.BLUE}query      {Fore.RESET}searches for notes
""")

operations = {
    "-h": lambda: print(helptext),
    "-d": delete_note,
    "-e": edit_note,
    "-s": search_notes,
}


def display_note(title: str):
    notes = nts.load_notes()

    try:
        content = notes[title]
    except KeyError:
        print(f("{Fore.RED}Note not found. Run with -h for help."))
        return 1

    md = consolemd.Renderer()
    md.render(f("# {title}\n\n{content}"))

    return 0


def main(args: List[str]) -> int:
    init()  # colorama

    if len(args) <= 1:
        return create_note()

    if args[1] in operations:
        try:
            return operations[args[1]](args[2])
        except IndexError:
            return operations[args[1]]()

    args.pop(0)
    return display_note(" ".join(args))


def run():  # blame setup.py for this
    exit(main(sys.argv))


if __name__ == "__main__":
    run()
