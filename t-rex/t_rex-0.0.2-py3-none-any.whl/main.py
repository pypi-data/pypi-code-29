from prompt_toolkit.application import Application
from prompt_toolkit.layout.layout import Layout
from .layout import root_container, cmd_window
from .keybindings import kb

application = Application(
        layout=Layout(root_container, focused_element=cmd_window),
        key_bindings=kb,
        mouse_support=True,
        full_screen=True)

if __name__ == '__main__':
    application.run()
