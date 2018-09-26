import asyncio
import json
import logging
import signal
import uuid
from abc import ABCMeta, abstractmethod
from asyncio import Future
from collections import namedtuple
from enum import Enum
from pathlib import Path
from typing import List

from .util import _terminate_or_kill

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)
log.addHandler(logging.StreamHandler())


class Align(Enum):
    """
    Represents the different alignments a module can have
    """
    LEFT = 'l'
    CENTER = 'c'
    RIGHT = 'r'


class Bar:
    """
    Class representing an instance of lemonbar. The output on the lemonbar is defined by
    registering modules (instances of `BarModule`) on an instance of this class.
    """
    _ModuleUpdate = namedtuple('_ModuleUpdate', ['contents', 'module', 'key', 'new_updater'])

    def __init__(self,
                 fonts=None,
                 bg_color='#000000',
                 fg_color='#FFFFFF',
                 u_color='#FF0000',
                 screen_bottom=False,
                 geometry=None,
                 padding=(0, 0),
                 spacing=0,
                 offset=0,
                 separator='',
                 _loop=None,
                 config_file=None):
        """
        :param font: The default font of the bar, as would be passed to fc-match

        :param bg_color: Default background color for the bar
        :param fg_color: Default foreground color for the bar
        :param u_color: Default underline color for the bar

        :param screen_bottom: If True, show the bar at the bottom of the screen

        :param geometry: Determines the size and positioning of the bar. 4-tuple containing
            (width, height, x-offset, y-offset). This is passed directly to lemonbar's -g
            parameter

        :param padding: The spacing before and after the first and last elements of the
            bar respectively.

        :param spacing: The spacing around each element

        :param offset: Vertical offset for the text, in pixels. Positive means up, negative means down

        :param separator: The character separating each element. It is inserted in the
            middle of the spacing

        :param config_file: Path to a json config file from which colors will be read. If
            `None`, no config file will be used. If the config file *is* supplied, then,
            whenever it changes, the bar will be reloaded with the new settings. The config file
            is stored as a a dict in `Bar.config`
        """

        self.bg_color = bg_color
        self.fg_color = fg_color
        self.u_color = u_color
        self.screen_bottom = screen_bottom
        self.fonts = fonts or []
        self.geometry = geometry
        self.padding = padding
        self.spacing = spacing
        self.offset = offset
        self.separator = separator

        if config_file is not None:
            self.config_file = Path(config_file)
            self.read_config_file(self.config_file)
        else:
            self.config_file = None

        self.module_updaters = []

        self.modules = {
            Align.LEFT: [],
            Align.CENTER: [],
            Align.RIGHT: []
        }

        self.outputs = {
            Align.LEFT: {},
            Align.CENTER: {},
            Align.RIGHT: {}
        }

        self.button_callbacks = {}

        self.loop: asyncio.AbstractEventLoop = _loop or asyncio.get_event_loop()

    def register_module(self, module):
        """Register the module on the bar."""

        if module.align not in list(Align):
            log.error('align property must be one of Align.{LEFT,CENTER,RIGHT}.')
            raise SystemExit(1)

        self.modules[module.align].append(module)
        output_key = len(self.modules[module.align])

        async def updater():
            return self._ModuleUpdate(
                contents=await module.get_output(),
                module=module,
                key=output_key,
                new_updater=updater
            )

        async def first_updater(): 
            return self._ModuleUpdate(
                contents=await module.setup(self),
                module=module,
                key=output_key,
                new_updater=updater
            )

        self.module_updaters.append(first_updater)

    def register_button(self, button):
        """
        Register a button on the bar.
        """
        for id, button, callback in button.callbacks:
            self.button_callbacks[id] = callback

    def button(self, *args, **kwargs):
        """
        Create a Button and register it on the bar. This is basically equivalent to

        >>> bar = Bar()
        >>> button = Button('button text', (1, lambda: print('hello')))
        >>> bar.register_button(button)

        All arguments passed in to this function are passed directly to `Button`.
        :returns: The created button
        """
        button = Button(*args, **kwargs)
        self.register_button(button)
        return button

    def read_config_file(self, path):
        """
        Read a json config file and apply it to this bar instance. The contents of this file
        (as a dict) are stored in `Bar.config`

        :param path: A `Path` object pointing to the config file
        """
        log.debug('Reading config file')
        config = json.loads(path.read_text())
        self.config = config

        self.bg_color = config.get('background', self.bg_color)
        self.fg_color = config.get('foreground', self.fg_color)
        self.u_color = config.get('underline', self.u_color)

    def run(self):
        """
        Start the bar. Make sure you call this after registering all the modules you need as
        this is going to block the program until the bar is stopped
        """
        log.debug('Starting event loop')
        self.loop.create_task(self._start_and_run())
        self.loop.run_forever()

    async def _write_to_bar(self, output):
        # Stop this if bar dies
        if self._bar.returncode is not None:
            self.loop.stop()
            return
        self._bar.stdin.write(bytes(output, 'utf8') + b'\n')

    async def _update_bar(self):
        """
        Combine all module outputs with appropriate formatting and write the result to the
        bar's stdin
        """
        spacing = f'%{{O{self.spacing/2}}}{self.separator}%{{O{self.spacing/2}}}'
        output = ('%{l}'
                  + f'%{{O{self.padding[0]}}}'
                  + spacing.join(str(v) for k, v in sorted(self.outputs[Align.LEFT].items()))

                  + '%{c}'
                  + spacing.join(str(v) for k, v in sorted(self.outputs[Align.CENTER].items()))

                  + '%{r}'
                  + spacing.join(str(v) for k, v in sorted(self.outputs[Align.RIGHT].items()))

                  + f'%{{O{self.padding[1]}}}')  # yapf: disable

        log.debug(f'TEXT: {output}')

        await self._write_to_bar(output)

    async def _start_bar(self):
        """
        Start the bar process with the arguments as specified by the object's fields
        """

        args = [
            "/usr/bin/lemonbar", '-p',
            '-B', self.bg_color,
            '-F', self.fg_color,
            '-U', self.u_color,
            '-o', str(self.offset)
        ] # yapf: disable

        if self.geometry:
            w, h, x, y = self.geometry
            args += ['-g', f'{w}x{h}+{x}+{y}']

        if self.screen_bottom:
            args += ['-b']

        for font in self.fonts:
            args += ['-f', font]

        log.info('Starting bar process: ')
        log.info(' '.join(args))
        self._bar = await asyncio.create_subprocess_exec(
            *args, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)

    async def _restart_bar(self):
        """
        Terminate the bar and then start it again. Updates it right after restarting, so
        that the newly started bar looks like the one that was just killed
        """
        if await _terminate_or_kill(self._bar, 2):
            log.debug('Bar terminated')
        else:
            log.debug('Bar killed')
        await self._start_bar()
        log.debug('started')
        await self._update_bar()

    async def _button_handler(self):
        """
        Continuously waits for output from the lemonbar process. When it is received,
        dispatches the appropriate handler from `self.button_callbacks`.
        """
        while True:
            id = (await self._bar.stdout.readline()).decode().strip()
            # When we are restarting the bar, readline will receive empty lines. In order
            # not to starve other coroutines by repeatedly waiting for bar stdout, pause
            # this for a second
            if id == '':
                log.debug(
                    'Empty line received, taken as bar reloading. Pausing button handler')
                await asyncio.sleep(1)
                continue
            try:
                self.button_callbacks[id]()
            except KeyError:
                log.warn(f'Received button id "{id}" but it has not been registered')

    def _handle_usr1(self):
        """
        Read the config file and restart the bar process
        """
        if self.config_file is not None:
            log.info('USR1 Received. Reloading config')
            try:
                self.read_config_file(self.config_file)
            except FileNotFoundError:
                log.warning(f'Tried to read config file {self.config_file!s} but it did not'
                            'exist. No changes made')
            else:
                log.debug('Config reload completed, restarting bar')
                # restart
                self.loop.create_task(self._restart_bar())
        else:
            log.info('USR1 Received, but there is no config file, ignoring')

    async def _updater(self):
        update_coroutines = {updater() for updater in self.module_updaters}

        while True:
            done, pending = await asyncio.wait(
                list(update_coroutines), return_when=asyncio.FIRST_COMPLETED)

            update_coroutines = pending

            for future in done:
                try:
                    update = future.result()
                    if update.contents is not None:
                        self.outputs[update.module.align][update.key] = update.contents
                    update_coroutines.add(update.new_updater())
                except Exception:
                    log.exception("A module raised an exception and has been stopped")
            await self._update_bar()

    async def _start_and_run(self):
        """
        Start the bar process, register updaters, button handlers, and signal handlers
        """
        await self._start_bar()

        self.loop.create_task(self._updater())
        self.loop.create_task(self._button_handler())

        self.loop.add_signal_handler(signal.SIGUSR1, self._handle_usr1)


class Button:
    """
    A button on the lemonbar.

    It can respond to multiple buttons with different callbacks. In order to perform its
    action when clicked it must be registered on a `Bar` instance first. Then it can be
    shown on the bar by calling `str` on it and outputing it from a module.

    The following example would show a button with the text "Say hi" on the bar which would
    output "hi" to stdout whenever clicked

    >>> bar = Bar()
    >>> button = Button('Say hi', (1, lambda: print('hi')))
    >>> bar.register_button(button)
    >>> bar.register_module(ConstantModule(button))
    >>> bar.run()
    """

    def __init__(self, text, *callbacks):
        """
        :param text: The text on the button
        :param callbacks: A list of (button, callback) tuples, determining which callback
            gets called when the button is clicked with each mouse button. See man(1)
            lemonbar for the button ids
        """
        self.text = text

        # if just button, callback was passed in
        if isinstance(callbacks[0], int):
            callbacks = [callbacks]

        self.callbacks = [(uuid.uuid4().hex[:8], button, cb) for button, cb in callbacks]

    def __str__(self):
        output = ''
        for id, button, _ in self.callbacks:
            output += f'%{{A{button}:{id}:}}'
        output += self.text
        output += ''.join('%{A}' for _ in self.callbacks)
        return output


class BarModule(metaclass=ABCMeta):
    """
    A lemonbar module.  It must be attached to a `Bar` instance to produce its output.

    This is an Abstract Base Class. To instantiate it you must override setup and
    get_output, both of which are async methods.

    Note that a few subclasses of this module are available in :py:mod:`~squeezer.modules`
    which will simplify the creation of modules for specific usecases.
    """

    def __init__(self,
                 align=Align.LEFT,
                 padding=0,
                 bg_color=None,
                 fg_color=None,
                 u_color=None):
        """
        :param align: One of the values in `Align`. Whether the bar should be align to the
            left, center or right of the bar
        :param bg_color: Background color of the module
        :param fg_color: Foreground color of the module
        :param u_color: Underline color of the module
        :param padding: Internal padding for the module
        """

        self.align = align
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.u_color = u_color
        self.padding = padding

    def format_string(self, string, fg_reset, bg_reset, u_reset):
        """
        Format a string according to the module's parameters (fg_color, bg_color, u_color)
        """
        output = string

        if self.padding:
            output = f'%{{O{self.padding}}}{output}%{{O{self.padding}}}'

        if self.bg_color:
            output = backgrounded(output, self.bg_color, bg_reset)
        if self.fg_color:
            output = colored(output, self.fg_color, fg_reset)
        if self.u_color:
            output = underlined(output, self.u_color, u_reset)

        return output

    async def get_formatted_output(self, fg_reset, bg_reset, u_reset):
        """
        Call self.get_output and format the return value according the this module's
        parameters
        """
        return self.format_string(await self.get_output(), fg_reset, bg_reset, u_reset)

    async def formatted_setup(self, bar, fg_reset, bg_reset, u_reset):
        """
        Call self.setup and format the return value according the this module's parameters
        """
        return self.format_string(await self.setup(bar), fg_reset, bg_reset, u_reset)

    @abstractmethod
    async def setup(self, bar):
        """
        Initial setup of the module. This is awaited **once** when the bar is started. The
        return value is set as the module text. If None, the initial module text will be
        'None'

        :param bar: Receives the `Bar` instance to which the module is attached
        """
        pass

    @abstractmethod
    async def get_output(self):
        """
        Main updating method. This should return the text of the module every time it
        returns. Whenever it completes its return value is shown (as defined by the Module's
        properties) on the bar and it is awaited again.

        Returning None means the bar should not be updated
        """
        pass


def colored(text, color=None, reset_color=None):
    """
    Colorize text for showing on the bar

    :param text: The text to colorize
    :param color: The color in "#RGB", "#RRGGBB" or "#AARRGGBB" format. Defaults to the
        default color of the bar
    :param reset_color: The color to reset to after this text. Defaults to the default color
        of the bar
    """
    reset_color = reset_color or '-'
    color = color or '-'
    return f'%{{F{color}}}{text!s}%{{F{reset_color}}}'


def backgrounded(text, color=None, reset_color=None):
    """
    Set background color of text for showing on the bar

    :param text: The text to colorize
    :param color: The background color in "#RGB", "#RRGGBB" or "#AARRGGBB" format. Defaults
        to the default background color of the bar
    :param reset_color: The background color to reset to after this text. Defaults to the
        default background color of the bar
    """
    reset_color = reset_color or '-'
    color = color or '-'
    return f'%{{B{color}}}{text!s}%{{B{reset_color}}}'


def underlined(text, color=None, reset_color=None):
    """
    Set background color of text for showing on the bar

    :param text: The text to colorize
    :param color: The underline color in "#RGB", "#RRGGBB" or "#AARRGGBB" format. Defaults
        to the default underline color of the bar
    :param reset_color: The underline color to reset to after this text. Defaults to the
        default underline color of the bar
    """
    reset_color = reset_color or '-'
    color = color or '-'
    return f'%{{U{color}}}%{{+u}}{text!s}%{{-u}}%{{U{reset_color}}}'
