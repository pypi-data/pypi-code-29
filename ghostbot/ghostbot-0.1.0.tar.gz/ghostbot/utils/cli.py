from __future__ import unicode_literals
from prompt_toolkit.application import Application
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.filters import IsDone
from prompt_toolkit.layout.controls import TokenListControl
from prompt_toolkit.layout.containers import ConditionalContainer, ScrollOffsets, HSplit
from prompt_toolkit.layout.dimension import LayoutDimension as D
from prompt_toolkit.mouse_events import MouseEventTypes
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict

# セレクトアイテム
choices = ['ls', 'ifconfig', 'pwd', 'who']
# 質問文
string_query = ' Command Select '
# 操作説明
inst = ' (Use arrow keys)'

# 選択した際に実行する関数
def selected_item(text):
    # クリップボードにコピー
    # 必要 : pip install pyperclip
    import pyperclip
    pyperclip.copy(text)
    # Command実行
    import subprocess
    res = subprocess.call(text)
    print(res)


# 以下セレクタ実装

# マウス操作が入った時に落とすためのデコレータ
def if_mousedown(handler):
    def handle_if_mouse_down(cli, mouse_event):
        if mouse_event.event_type == MouseEventTypes.MOUSE_DOWN:
            return handler(cli, mouse_event)
        else:
            return NotImplemented
    return handle_if_mouse_down

# セレクトアイテムを受け取って選択させるための制御Class
# controlsのTokenListControlを継承する
class InquirerControl(TokenListControl):
    selected_option_index = 0
    answered = False
    choices = []

    def __init__(self, choices, **kwargs):
        self.choices = choices
        super(InquirerControl, self).__init__(self._get_choice_tokens, **kwargs)

    @property
    def choice_count(self):
        return len(self.choices)

    def _get_choice_tokens(self, cli):
        tokens = []
        T = Token

        def append(index, label):
            selected = (index == self.selected_option_index)

            @if_mousedown
            def select_item(cli, mouse_event):
                # bind option with this index to mouse event
                self.selected_option_index = index
                self.answered = True
                cli.set_return_value(None)

            token = T.Selected if selected else T
            tokens.append((T.Selected if selected else T, ' > ' if selected else '   '))
            if selected:
                tokens.append((Token.SetCursorPosition, ''))
            tokens.append((T.Selected if selected else T, '%-24s' % label, select_item))
            tokens.append((T, '\n'))

        for i, choice in enumerate(self.choices):
            append(i, choice)
        tokens.pop()  # Remove last newline.
        return tokens

    def get_selection(self):
        return self.choices[self.selected_option_index]

# インスタンス生成
ic = InquirerControl(choices)

# prompt情報の取得
def get_prompt_tokens(cli):
    tokens = []
    T = Token
    tokens.append((Token.QuestionMark, '?'))
    tokens.append((Token.Question, string_query))
    if ic.answered:
        # 選択した値を取得
        tokens.append((Token.Answer, ' ' + ic.get_selection()))
        # 任意関数実行
        selected_item(ic.get_selection())
    else:
        tokens.append((Token.Instruction, inst))
    return tokens


# 疑似レイアウトをトークンリストから設定
layout = HSplit([
    Window(height=D.exact(1),
           content=TokenListControl(get_prompt_tokens, align_center=False)),
    ConditionalContainer(
        Window(
            ic,
            width=D.exact(43),
            height=D(min=3),
            scroll_offsets=ScrollOffsets(top=1, bottom=1)
        ),
        filter=~IsDone())])

# keyバインディングの設定
manager = KeyBindingManager.for_prompt()
@manager.registry.add_binding(Keys.ControlQ, eager=True)
@manager.registry.add_binding(Keys.ControlC, eager=True)
def _(event):
    event.cli.set_return_value(None)
@manager.registry.add_binding(Keys.Down, eager=True)
def move_cursor_down(event):
    ic.selected_option_index = (
        (ic.selected_option_index + 1) % ic.choice_count)
@manager.registry.add_binding(Keys.Up, eager=True)
def move_cursor_up(event):
    ic.selected_option_index = (
        (ic.selected_option_index - 1) % ic.choice_count)
@manager.registry.add_binding(Keys.Enter, eager=True)
def set_answer(event):
    ic.answered = True
    event.cli.set_return_value(None)

# Color Font Style
inquirer_style = style_from_dict({
    Token.QuestionMark: '#5F819D',
    Token.Selected: '#FF9D00',
    Token.Instruction: '',
    Token.Answer: '#FF9D00 bold',
    Token.Question: 'bold',
})

# layoutを選択モデルにしたAppを設定
app = Application(
    layout=layout,
    key_bindings_registry=manager.registry,
    mouse_support=True,
    style=inquirer_style
)

# eventloopで実行、終了時close
eventloop = create_eventloop()
try:
    cli = CommandLineInterface(application=app, eventloop=eventloop)
    cli.run(reset_current_buffer=False)
finally:
    eventloop.close()