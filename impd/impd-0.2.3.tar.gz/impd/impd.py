#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
impd is a basic Gtk interface for mpd

    Copyright (C) 2018  Steven J. Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

see full license at ../LICENSE.txt
"""

import argparse
import os
import logging

import yaml

# from impd import client as impd_client
from impd import ui


DEFAULT_WIDTH = 300
SETTINGS_PATH = os.path.expanduser('~/.impd/settings.yaml')
MPD_SETTINGS = os.path.expanduser('~/.mpd/mpd.conf')
ARTFOLDER = os.path.expanduser('~/.impd/covers')
COVER_ORDER = 'folder,ffmpeg,musicbrainz'
COVER_REGEX = '(cover|artwork|folder)\.(jpg|png)'
LOGGER = logging.getLogger('impd')


def load_settings(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        data = f.read()
    return yaml.load(data)


def load_mpd_settings(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        data = f.read()
    skip = False
    output = {}
    for line in data.splitlines():
        line = line.strip('\t ')
        if line == '}':
            skip = False
            continue
        if '"' not in line or skip:
            continue
        key, value, _ = line.split('"')
        key = key.strip('\t ')
        output[key] = value
    return output


def load_arguments():
    h_host = 'The hostname to connect to mpd.'
    h_port = 'The port to connect to mpd.'
    h_width = 'The width of the entire window.'
    h_interval = 'The delay between each time update, In seconds..'
    h_fade_in = 'The amount to add on each step of the fade in.'
    h_fade_out = 'The amount to add on each step of the fade out.'
    h_artwork = 'The folder to store artwork in. Default is ~/.impd/covers/'
    h_verbose = 'Turns on verbose mode.'
    h_icon_width = 'The width if playlist artwork icons.'
    h_icon_missing_width = ('The padding of the text '
                            'if a playlist item has no icon. '
                            'This is used for alignment.')
    h_player_opacity = 'The max opacity of the player controls and background.'
    h_mpd_settings = ('The location of your mpd.conf, '
                      'This is required if you want local '
                      'artwork to be found.')
    h_cover_order = ('The order of methods to find cover artwork. '
                     'The default is "{}"'.format(COVER_ORDER))
    h_cover_regex = ('The regex to use to find local artworks '
                     'inside your music folder. '
                     'Default is "{}"'.format(COVER_REGEX))

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', '-H', default=None, help=h_host)
    parser.add_argument('--port', '-p', type=int, default=None, help=h_port)
    parser.add_argument('--width', '-w', type=int, default=None, help=h_width)
    parser.add_argument('--interval', '-I', type=int, default=None,
                        help=h_interval)
    parser.add_argument('--fade_in', '-f', type=int, default=None,
                        help=h_fade_in)
    parser.add_argument('--fade_out', '-F', type=int, default=None,
                        help=h_fade_out)
    parser.add_argument('--artwork', '-a', default=None, help=h_artwork)
    parser.add_argument('--verbose', '-v', default=None, action='store_true',
                        help=h_verbose)
    parser.add_argument('--icon_width', '-s', default=None, help=h_icon_width)
    parser.add_argument('--icon_missing_width', '-S', default=None,
                        help=h_icon_missing_width)
    parser.add_argument('--player_opacity', '-o', type=int, default=None,
                        help=h_player_opacity)
    parser.add_argument('--mpd_settings', '-c', default=None,
                        help=h_mpd_settings)
    parser.add_argument('--cover_order', '-C', default=None,
                        help=h_cover_order)
    parser.add_argument('--cover_regex', '-r', default=None,
                        help=h_cover_regex)
    parser.add_argument('--force_mini', '-m', default=None,
                        action='store_true')
    parser.add_argument('--hide_scrollbar', '-b', default=None,
                        action='store_true')
    args = parser.parse_args()

    settings = load_settings(SETTINGS_PATH)

    arguments = {
        'host': (args.host or settings.get('host', None)
                 or os.getenv('MPD_HOST', 'localhost')),
        'port': (args.port or settings.get('port', None)
                 or os.getenv('MPD_PORT', 6660)),
        'width': args.width or settings.get('width', DEFAULT_WIDTH),
        'update_interval': args.interval or settings.get('interval', 1),
        'fade_in': args.fade_in or settings.get('fade_in', 10),
        'fade_out': args.fade_out or settings.get('fade_out', 10),
        'artwork_folder': args.artwork or settings.get('artwork', ARTFOLDER),
        'verbose': args.verbose or settings.get('verbose', False),
        'icon_width': int(args.icon_width or settings.get('icon_width', 35)),
        'icon_missing_width':
            int((args.icon_missing_width
                or settings.get('icon_missing_width', 20))),
        'player_opacity': int(args.player_opacity
                              or settings.get('player_opacity', 100)),
        'mpd_settings': (args.mpd_settings
                         or settings.get('mpd_settings', MPD_SETTINGS)),
        'cover_order': (args.cover_order
                        or settings.get('cover_order', COVER_ORDER)),
        'cover_regex': (args.cover_regex
                        or settings.get('cover_regex', COVER_REGEX)),
        'force_mini': (args.force_mini or settings.get('force_mini', False)),
        'hide_scroll': (args.hide_scrollbar
                        or settings.get('hide_scrollbar', False)),
    }

    mpd_path = arguments.get('mpd_settings', None)
    if mpd_path is not None:
        mpd_settings = load_mpd_settings(os.path.expanduser(mpd_path))
        for key, value in mpd_settings.items():
            arguments['mpd_{}'.format(key)] = value
    return arguments


def main():
    settings = load_arguments()

    if settings['verbose']:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.WARNING)

    window = ui.MainWindow(settings)
    window.main()
    return None
