from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import pkgutil


class MyCustomCompleter(Completer):
    def __init__(self):
        self.modules = pkgutil.iter_modules()
        self.modules = ["Aaa", "Bbb", "Ccc"]

    # prompt_toolkit.document.Document
    def get_completions(self, document, complete_event):

        for i in filter(lambda item: item.startswith(document.text_before_cursor), self.modules):
            yield Completion(i, start_position=-1)


def interactive():
    module_name = prompt("Select module name: ", completer=MyCustomCompleter())
