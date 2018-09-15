import os
import subprocess
from tempfile import NamedTemporaryFile
from typing import Tuple

from colorama import Fore

from nts.fstring import f
import nts.api as nts

note_template = """# Title

**This is a new note.** Edit this as you want, and close your editor to save.
Markdown formatting is supported, and the first line (excluding the hash) will
be the note title.

Looking for NTS help? Run with the `-h` argument.
"""


def _write_tempfile(name: str):
    with open(name, "w") as f:
        f.write(note_template)


def _get_edits(filename: str) -> str:
    editor = os.environ.get("EDITOR", "nano")  # todo: better way to find editor
    subprocess.call([editor, filename])
    with open(filename, "r") as f:
        return f.read()


def _split_data(content: str) -> Tuple[str, str]:
    title = content.splitlines()[0][1:].strip()
    note = "\n".join(content.splitlines()[1:]).strip()

    return title, note


def create_note() -> int:
    file = NamedTemporaryFile(suffix='.md')

    _write_tempfile(file.name)
    note_content = _get_edits(file.name)

    if note_content == note_template:
        print(f("{Fore.RED}No changes found, cancelled."))
        return 1

    notes = nts.load_notes()
    notes = nts.edit_note(notes, *_split_data(note_content))
    nts.save_notes(notes)
    print(f("{Fore.GREEN}Saved."))

    return 0

