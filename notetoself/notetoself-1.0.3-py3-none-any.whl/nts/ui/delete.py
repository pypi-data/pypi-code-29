from colorama import Fore

from nts.fstring import f
import nts.api as nts


def delete_note(note: str) -> int:
    notes = nts.load_notes()
    try:
        notes = nts.delete_note(notes, note)
        nts.save_notes(notes)
    except KeyError:
        print(f("{Fore.RED}No such note!"))
        return 1

    print(f("{Fore.GREEN}Deleted."))
    return 0
