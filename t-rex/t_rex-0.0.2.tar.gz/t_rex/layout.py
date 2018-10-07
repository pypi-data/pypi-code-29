from prompt_toolkit.widgets import TextArea, SearchToolbar
from prompt_toolkit.layout import D
from prompt_toolkit.layout.containers import (VSplit,
        HSplit,
        FloatContainer,
        Float)
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.menus import CompletionsMenu

from .completer import redis_completer
from .executor import execute, ResultType, execute_subcommand

def cmd_handler(buf):
    text = buf.text
    if not text:
        return
    result_type, result = execute(text)
    if result_type == ResultType.DETAIL:
        wide_output.text = result
        narrow_output.text = ''
    elif result_type == ResultType.PATTERN:
        wide_output.text = ''
        narrow_output.text = result
    elif result_type == ResultType.ERROR:
        wide_output.text = result
        narrow_output.text = ''


def narrow_enter_handler(buf):
    # This should always put the results in the wide window.
    # If enter was handled from the wide window then copy wide into narrow and
    # place the results of subcommand in wide.
    text = buf.document.current_line
    if not text:
        return
    _, result = execute_subcommand(text)
    wide_output.text = result

def wide_enter_handler(buf):
    text = buf.document.current_line
    if not text:
        return
    _, result = execute_subcommand(text)
    narrow_output.text = wide_output.text
    wide_output.text = result


left_search_field = SearchToolbar()
right_search_field = SearchToolbar()

narrow_output = TextArea(search_field=left_search_field,
        read_only=True,
        focus_on_click=True,
        accept_handler=narrow_enter_handler,
        width=D(weight=30))
wide_output = TextArea(search_field=right_search_field,
        read_only=True,
        focus_on_click=True,
        accept_handler=wide_enter_handler,
        width=D(weight=70))
left_window = HSplit([narrow_output,
    left_search_field])

right_window = HSplit([wide_output,
    right_search_field])

vsep = Window(width=1, char='|', style='class:line')
hsep = Window(height=1, char='-', style='class:line')
cmd_window = TextArea(height=1, prompt='> ',
        completer=redis_completer,
        style='class:input-field',
        multiline=False,
        accept_handler=cmd_handler,
        focus_on_click=True)

body = VSplit([
    left_window,
    vsep,
    right_window,
    ])

root_container = FloatContainer(
        content=HSplit([
            cmd_window,
            hsep,
            body,
            ]),
        floats=[
            Float(xcursor=True,
                  ycursor=True,
                  content=CompletionsMenu(max_height=4, scroll_offset=1))
            ]
        )
