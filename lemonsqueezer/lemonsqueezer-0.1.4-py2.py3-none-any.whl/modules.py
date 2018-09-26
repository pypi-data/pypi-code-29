"""
A set of premade, parameterized modules to cover some of the most common
usecases for the lemonbar
"""

from abc import abstractmethod, ABCMeta
from asyncio.subprocess import PIPE
import asyncio
import string
import subprocess
from typing import List
import re

import lemonsqueezer as lsq

import logging


def _get_cmd_output(*args, **kwargs):
    """
    get a command's output using `subprocess.run`. `args` specify the command to be run,
    while `kwargs` get passed directly to subprocess.run
    """
    return subprocess.run(args, stdout=PIPE, **kwargs).stdout.decode()


class ConstantModule(lsq.BarModule):
    """ 
    Show a constant string on the bar. Can be used for simple buttons
    """
    def __init__(self, text, *args, _loop=None, **kwargs):
        """
        :param text: The string to show on the bar
        """
        super().__init__(*args, **kwargs)
        self.text = text

        self._lock = asyncio.Lock(loop=_loop)

    # show it once...
    async def setup(self, bar):
        await self._lock.acquire()
        return self.text

    # ...and the wait forever
    async def get_output(self):
        await self._lock.acquire()


class PeriodicModule(lsq.BarModule, metaclass=ABCMeta):
    """
    Show text on the bar that updates every few seconds. This is the way most
    other bars/bar managers work. Before using this, see if
    :class:`~lemonsqueezer.modules.CommandMonitorModule` can be used instead, as
    it can be much more efficient
    """
    def __init__(self, interval, *args, **kwargs):
        """
        :param interval: How often to update the module
        """
        super().__init__(*args, **kwargs)
        self.interval = interval

    async def setup(self, bar):
        return self.on_update()

    async def get_output(self):
        await asyncio.sleep(self.interval)
        return self.on_update()

    @abstractmethod
    def on_update(self):
        """
        This is run on every update.

        Return the new text to be displayed on the bar, or None, if no update
        should be made
        """
        pass


class CommandMonitorModule(lsq.BarModule, metaclass=ABCMeta):
    """
    A module that updates whenever a command produces a line of output. This can
    replace most modules that would update periodically to show system
    information, while being much more efficient as the bar is only written to
    when a change happens
    """
    def __init__(self, command_args: List[str], *args, **kwargs):
        """
        :param command_args: The command to be run as a list of strings
        """
        super().__init__(*args, **kwargs)
        self.command_args = command_args
        self._process = None

    async def setup(self, bar):
        self._process = await asyncio.create_subprocess_exec(
            *self.command_args, stdout=PIPE)
        return self.first_output(bar)

    async def get_output(self):
        if self._process.returncode is not None:
            raise BrokenPipeError
        process_output =\
            (await self._process.stdout.readline()).decode().strip()
        return self.on_line_received(process_output)

    @abstractmethod
    def first_output(self, bar):
        """
        Run immediately when the bar is started. Receives the bar instance as an
        argument. The return value is set as the text of the module.
        """
        return '-'

    @abstractmethod
    def on_line_received(self, process_output):
        """
        Run whenever the command outputs a full line of output. 
        Receives that output as an argument. The return value of this function
        is shown on the module.
        """
        return ''


class TickTock(PeriodicModule):
    """
    Test module. Switches between tick and tock every time an interval passes
    """
    def __init__(self, interval, *args, **kwargs):
        """
        :param interval: How often to switch between "tick" and "tock"
        """
        super().__init__(interval, *args, **kwargs)
        self.tick = False

    def on_update(self):
        self.tick = not self.tick
        return 'tick' if self.tick else 'tock'


class Clock(PeriodicModule):
    """
    A clock based on the 'date' command
    """
    def __init__(self, format_str, interval, icon='', *args, **kwargs):
        """
        :param format_str: The format string to pass to the 'date' command
        :param interval: How often to update the call
        """
        super().__init__(interval, *args, **kwargs)
        self.format_str = format_str
        self.icon = icon

    def on_update(self):
        out = _get_cmd_output('date', self.format_str).strip()
        return f'{self.icon} {out}'


class Counter(lsq.BarModule):
    """
    Test module: A counter that increases, decreases or resets 
    """
    async def setup(self, bar):
        self.count = 0
        self.inc_lock = asyncio.Lock()
        await self.inc_lock.acquire()

        def inc():
            self.count += 1
            self.inc_lock.release()

        def dec():
            self.count -= 1
            self.inc_lock.release()

        def reset():
            self.count = 0
            self.inc_lock.release()

        self.button = lsq.Button(
            str(self.count), (1, inc), (2, reset), (3, dec))
        bar.register_button(self.button)

        return self.button

    async def get_output(self):
        await self.inc_lock.acquire()
        self.button.text = str(self.count)
        return self.button


class BSPWMDesktops(CommandMonitorModule):
    """
    A module for showing desktops for bspwm. Shows every desktop by name and highlights the
    current one.
    """

    def __init__(self, monitor_sel, highlight_color, *args, **kwargs):
        """
        :param monitor_sel: The monitor for which to display the desktops. Note that this
            is only used to get a monitor id which is then used to monitor desktop events.
            So, if you pass in 'focused', for example, the module will display the desktops
            for the monitor which was focused when the bar was launched.

        :param highlight_color: What color to highlight the active desktop with.
        """
        super().__init__(['bspc', 'subscribe', 'report'], *args, **kwargs)

        self.highlight_color = highlight_color
        self.monitor_sel = monitor_sel

        self.monitor_name = _get_cmd_output(
                'bspc', 'query', '-M', '-m', monitor_sel, '--names').strip()

        # Maps desktop names to buttons
        self.desktops = {}
        self.focused_desktop = _get_cmd_output(
                'bspc', 'query', '-D', '-d', 'focused', '--names')

        # We need to maintain a reference to reattach the buttons whenever they are
        # recreated (when the desktop list changes)
        self._bar = None

    def parse_bspc_report(self, report):
        """
        Parse the output of `bspc subscribe report`

        :return: A dict containing the following fields
            * `monitor`: The name of the monitor the report refers to
            * `monitor_focused`: Bool, depends on whether the relevant monitor is focused
            * `desktops`: Dict from the names of the desktop on the monitor to a tuple
            representing their status. The tuple can contain the following values:
            'occupied', 'free', 'urgent', 'focused', 'unfocused'
        """

        # Report format WMDP1:f:O:o:f:fDesktop:LT:TT:G:meDP1:FDesktop:LT
        # See man(1) bspc for more details
        fields = report.strip('W ').split(':')

        adding = False
        status = {
            'desktops': {}
        }
        for field in fields:
            if not (adding or field == f'M{self.monitor_name}'
                    or field == f'm{self.monitor_name}'):
                continue

            # Relevant monitor section starts
            if field == f'M{self.monitor_name}' or field == f'm{self.monitor_name}':
                adding = True
                status['monitor'] = field[1:]
                status['monitor_focused'] = field[0] == 'M'

            # Some other monitor section starts
            elif field[0] in ['m', 'M']:
                adding = False

            # We are inside the relevant monitor section
            elif adding:
                if field[0] == 'O':
                    status['desktops'][field[1:]] = ('occupied', 'focused')
                elif field[0] == 'F':
                    status['desktops'][field[1:]] = ('free', 'focused')
                elif field[0] == 'U':
                    status['desktops'][field[1:]] = ('urgent', 'focused')
                elif field[0] == 'o':
                    status['desktops'][field[1:]] = ('occupied', 'unfocused')
                elif field[0] == 'f':
                    status['desktops'][field[1:]] = ('free', 'unfocused')
                elif field[0] == 'u':
                    status['desktops'][field[1:]] = ('urgent', 'unfocused')

        return status

    def make_desktop_buttons(self, bar, desktop_names):
        # Just used in the comprehension to create a callback for changing to each desktop
        def desktop_switch_callback(desktop_name):
            return lambda: subprocess.run(['bspc', 'desktop', '-f', desktop_name])

        def desktop_remove_callback(desktop_name):
            def func():
                new_desktops = list(self.desktops.keys())
                new_desktops.remove(desktop_name)
                subprocess.run(['bspc', 'monitor', 'focused', '--reset-desktops', *new_desktops])
            return func

        return [
            bar.button(name, (1, desktop_switch_callback(name)), (3, desktop_remove_callback(name)))
            for name in desktop_names
        ]

    def make_output(self, desktops, current_desktop):
        formatted_buttons = [
            lsq.colored(str(button), self.highlight_color)
            if name == current_desktop else str(button)
            for name, button in desktops.items()
        ]
        return ' | '.join(formatted_buttons)

    # BarModule methods

    def first_output(self, bar):
        self._bar = bar
        return self.make_output(self.desktops, self.focused_desktop)

    def on_line_received(self, report):
        # See `parse_bspc_report` docstring
        status = self.parse_bspc_report(report)

        # Flag for whether something had changed
        should_update = False

        if list(status['desktops'].keys()) != list(self.desktops.keys()):
            should_update = True

            new_desktops = status['desktops'].keys()
            self.desktops = dict(zip(
                new_desktops,
                self.make_desktop_buttons(self._bar, new_desktops)))

        try:
            new_focused_desktop = next(
                desktop
                for desktop, state in status['desktops'].items()
                if 'focused' in state)
        except StopIteration:
            # If we couldn't find the focused desktop for some reason, log and don't update
            lsq.log.warn('Could not find focused desktop in bspc report, not updating')
            lsq.log.debug(f'Report that caused error: \n{report}')
            raise ValueError()

        if new_focused_desktop != self.focused_desktop:
            should_update = True
            self.focused_desktop = new_focused_desktop

        if should_update:
            return self.make_output(self.desktops, self.focused_desktop)
        else:
            return None


class CurrentWifi(CommandMonitorModule):
    """
    Show the currently connected to SSID for a networkmanager device. Uses nmcli
    """
    def __init__(self, device, icon, *args, **kwargs):
        """
        :param device: Which device to monitor
        :param icon: A string to show before the SSID. Can be used to show a
            fontawesome icon
        """
        super().__init__(['nmcli', 'device', 'monitor', device], *args,
                         **kwargs)
        self.device = device
        self.icon = icon
        self.connecting_to = ''
        self.current_connection = '-'

    def first_output(self, bar):
        nmcli_show_output = _get_cmd_output('nmcli', '--terse', 'device',
                                            'show', self.device)

        # connection name is on the line starting with GENERAL.CONNECTION:
        try:
            self.current_connection = next(
                l.split(':')[1] for l in nmcli_show_output.splitlines()
                if l.split(':')[0] == 'GENERAL.CONNECTION')
        except StopIteration:
            self.current_connection = '-'

        return f'{self.icon} {self.current_connection}'

    
    connection_re = re.compile("'(.*)'")
    def on_line_received(self, event):
        if 'disconnected' in event:
            self.current_connection = '-'
        elif 'using connection' in event:
            self.connecting_to = self.connection_re.findall(event)[0]
        elif 'connected' in event and self.connecting_to != '':
            self.current_connection = self.connecting_to
            self.connecting_to = ''

        return f'{self.icon} {self.current_connection}'


class Battery(PeriodicModule):
    """
    Show current battery percentage using the `acpi` command
    """
    def __init__(self, icons, interval=20, *args, **kwargs):
        """
        :param icons: A list of string to show before the percentage depending
            on it. E.g. `["...", "..", "."]` would show ... between 100% and
            66%, .. between 66% and 33%, and . below 33%.
        :param interval: How often to update the battery level
        """
        super().__init__(interval, *args, **kwargs)
        self.icons = icons

    def _get_icon(self, battery_level):
        idx = min(len(self.icons)-1, battery_level // (100 // len(self.icons)))
        return self.icons[idx]

    def on_update(self):
        out = _get_cmd_output('acpi', '-b').strip()
        battery_level = int(out.split(', ')[1][:-1])
        icon = self._get_icon(battery_level)

        return f'{icon} {battery_level}%'


class MediaControls(CommandMonitorModule):
    """
    Shows current track information and provides play/pause/skip/rewind buttons.

    Needs `playerctl` available on the system
    """

    def __init__(self,
                 format_str='{artist} - {title}',
                 button_icons=None,
                 icon='',
                 *args,
                 **kwargs):
        """
        :param format_str: String showing how to format current track data. Uses standard
            python formatting. Accepted fields are:
            * {artist}
            * {album_artist}
            * {title}
            * {album}
        :param button_icons: A 4-tuple containing strings for the play, pause, previous and
            next buttons, in that order. E.g. `('play', 'pause', 'prev', 'next')` would use
            the literal strings "play", "pause", "prev" and "next" as the button names.
            Use `None` as a button's value to disable it.
            If parameter is not supplied, no buttons will be shown
        :param icon: Text that is shown to the left of all the module output. Can be used
            for a fontawesome icon
        """
        super().__init__([
            'dbus-monitor', '--session', '--profile',
            'path=/org/mpris/MediaPlayer2,member=PropertiesChanged'
        ], *args, **kwargs)
        self.format_str = format_str

        # Find the fields the format string requires
        fmt = string.Formatter()
        self.required_fields = [
            field_name for _, field_name, _, _ in fmt.parse(format_str)
        ]

        self.icon = icon

        play_icon, pause_icon, prev_icon, next_icon = button_icons or (None,
                                                                       None,
                                                                       None)

        self.play_button = lsq.Button(
            play_icon, (1, lambda: subprocess.run(['playerctl', 'play'])))
        self.pause_button = lsq.Button(
            pause_icon, (1, lambda: subprocess.run(['playerctl', 'pause'])))
        self.next_button = lsq.Button(
            next_icon, (1, lambda: subprocess.run(['playerctl', 'next'])))
        self.prev_button = lsq.Button(
            prev_icon, (1, lambda: subprocess.run(['playerctl', 'previous'])))

    def _get_formatted_output(self):
        # Check whether music is playing or not. If it's neither then there is no active
        # music player and we can return empty output
        playing = _get_cmd_output('playerctl', 'status', stderr=PIPE).strip()
        if playing == 'Playing':
            play_pause_button = self.pause_button
        elif playing == 'Paused':
            play_pause_button = self.play_button
        else:
            return f'{self.icon} -'

        # Get the values of the fields needed for the format string
        field_values = {}
        for required_field in self.required_fields:
            if required_field == 'artist':
                field_values['artist'] = _get_cmd_output(
                    'playerctl', 'metadata', 'artist')
            elif required_field == 'album_artist':
                field_values['albumArtist'] = _get_cmd_output(
                    'playerctl', 'metadata', 'xesam:albumArtist')
            elif required_field == 'title':
                field_values['title'] = _get_cmd_output(
                    'playerctl', 'metadata', 'title')
            elif required_field == 'album':
                field_values['album'] = _get_cmd_output(
                    'playerctl', 'metadata', 'album')

        return (f'{self.icon} {self.format_str.format(**field_values)} '
                f'{self.prev_button} {play_pause_button} {self.next_button}')

    def first_output(self, bar):
        bar.register_button(self.play_button)
        bar.register_button(self.pause_button)
        bar.register_button(self.prev_button)
        bar.register_button(self.next_button)
        return self._get_formatted_output()

    def on_line_received(self, line):
        return self._get_formatted_output()
