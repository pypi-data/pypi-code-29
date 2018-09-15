"""
NTS API

Can be ran on its own (optional dependency: appdirs)
"""

import json
import os
from typing import Dict

try:
    from appdirs import user_data_dir
except ImportError:
    pass  # gets checked later on


NoteListType = Dict[str, str]


def find_notes(notes: NoteListType, query: str) -> NoteListType:
    """ Finds notes matching query """
    return {k: v for k, v in notes.items() if query in k or query in v}


def edit_note(notes: NoteListType, name: str, content: str):
    """ Modifies a note. (Wlil be created if that note doesn't exist) """
    notes[name] = content
    return notes


def delete_note(notes: NoteListType, name: str):
    """ Deletes note """
    del notes[name]
    return notes


def get_note_path():
    """ Gets the standard note path """

    root = os.path.join(os.environ["HOME"], ".local", "share", "nts")
    if user_data_dir:
        root = user_data_dir("nts")

    # todo: get rid of side effects
    if not os.path.exists(root):
        os.makedirs(root)

    return os.path.join(root, "notes.json")


def save_notes(notes: NoteListType):
    """ Saves notes into a standard folder """
    with open(get_note_path(), "w") as f:
        json.dump(notes, f)


def load_notes() -> NoteListType:
    """ Load notes from a standard folder """
    filename = get_note_path()

    if not os.path.exists(filename):
        return {}

    with open(filename, "r") as f:
        return json.load(f)

