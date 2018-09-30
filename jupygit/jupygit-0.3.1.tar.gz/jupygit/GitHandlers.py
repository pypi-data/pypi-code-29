import json
import os
from urllib.parse import parse_qs

from notebook.base.handlers import IPythonHandler

from .gitignore_manipulator import add_gitignore_entry
from .nb_manipulator import clean_nb


class GitRestoreHandler(IPythonHandler):
    file_suffix = "-jupygit___.ipynb"

    def post(self):
        data = parse_qs(self.request.body.decode('utf8'))
        dirty_path = data["path"][0]

        clean_path = dirty_path[:-len(self.file_suffix)] + ".ipynb"
        os.remove(clean_path)

        self.set_status(200)


class GitCleanHandler(IPythonHandler):
    file_suffix = "-jupygit___.ipynb"

    def post(self):
        data = parse_qs(self.request.body.decode('utf8'))
        clean_path = data["path"][0]
        add_gitignore_entry(os.path.dirname(clean_path))

        dirty_path = clean_path[:-6] + self.file_suffix

        with open(dirty_path, "r") as r:
            dirty = json.load(r)

        clean_nb(dirty)

        with open(clean_path, "w") as w:
            json.dump(dirty, w, indent=1)
            w.write("\n")  # Fix for the new line issue

        self.set_status(200)
