from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.enums import EditingMode
from .layout import cmd_window

kb = KeyBindings()

@kb.add('tab')
def _(event):
    focus_next(event)
    if event.app.layout.has_focus(cmd_window):
        event.app.editing_mode = EditingMode.EMACS
    else:
        event.app.editing_mode = EditingMode.VI

@kb.add('s-tab')
def _(event):
    focus_previous(event)
    if event.app.layout.has_focus(cmd_window):
        event.app.editing_mode = EditingMode.EMACS
    else:
        event.app.editing_mode = EditingMode.VI

@kb.add('c-d', filter=has_focus(cmd_window))
def _(event):
    if cmd_window.text.strip() == '':
        event.app.exit()
