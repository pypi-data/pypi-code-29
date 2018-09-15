from colorama import Fore

from nts.fstring import f
import nts.api as nts


def search_notes(query: str) -> int:
    notes = nts.load_notes()

    found = nts.find_notes(notes, query)
    for name in found.keys():
        print(f("{Fore.BLUE}* {Fore.RESET}{name}"))

    if not found:
        print(f("{Fore.RED}No notes found."))
