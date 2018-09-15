from tempfile import NamedTemporaryFile

from colorama import Fore

from nts.ui.create import _get_edits, _split_data
from nts.fstring import f
import nts.api as nts


def edit_note(note: str) -> int:
    notes = nts.load_notes()

    try:
        content = notes[note]
        title = note
    except KeyError:
        print(f("{Fore.RED}No such note!"))
        return 1

    file = NamedTemporaryFile(suffix='.md')
    with open(file.name, "w") as fi:
        fi.write(f("# {title}\n\n{content}"))

    note_content = _get_edits(file.name)

    notes = nts.load_notes()
    notes = nts.delete_note(notes, title)  # easy way to handle name changes
    notes = nts.edit_note(notes, *_split_data(note_content))
    nts.save_notes(notes)
    print(f("{Fore.GREEN}Saved."))
