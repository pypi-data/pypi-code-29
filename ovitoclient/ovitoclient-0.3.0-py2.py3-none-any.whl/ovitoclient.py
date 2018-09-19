#!/usr/bin/env ovitos
# -*- coding:utf-8 -*-
#
# ovitoclient.py
#
# Copyright (c) 2018
# Ben Lindsay <benjlindsay@gmail.com>
# Christian Tabedzki <cat159@scarletmail.rutgers.edu>

from ovito import dataset
from ovito.data import ParticleProperty
from ovito.io import import_file
from ovito.modifiers import SelectExpressionModifier
from ovito.modifiers import SliceModifier
from ovito.vis import TextLabelOverlay
from ovito.vis import Viewport
from ovito.vis import RenderSettings
from ovito.vis import TachyonRenderer
from ovito.vis import OpenGLRenderer
from PyQt5 import QtCore
import argparse
import os

IMAGE_TYPES = ['png', 'jpg', 'jpeg', 'tif', 'tiff']
MOVIE_TYPES = ['gif', 'avi', 'mov', 'mp4']
ALL_OUTPUT_TYPES = IMAGE_TYPES + MOVIE_TYPES

def main(args):
    if args.verbosity > 0:
        print("input file:       {}".format(args.input_file))
        print("output file:      {}".format(args.output_file))
    if args.verbosity == 2:
        print("dimensions:       {}".format(args.dimensions))
        print("renderer:         {}".format(args.renderer))
        print("particle size:    {}".format(args.particle_size))

    if args.renderer == 'tachyon':
        renderer = TachyonRenderer()
    elif args.renderer == 'opengl':
        renderer = OpenGLRenderer()
    else:
        raise ValueError("{} is not a valid renderer".format(args.renderer))
    node = import_file(args.input_file, multiple_frames = True)
    node.add_to_scene()
    vp = dataset.viewports.viewports[args.viewport]
    if args.output_ext in MOVIE_TYPES and args.frames_per_second is not None:
        dataset.anim.frames_per_second = args.frames_per_second
    node.compute()
    if args.overlay_frame_num == True:
        overlay = TextLabelOverlay(
            text = '[SourceFrame]',
            alignment = QtCore.Qt.AlignRight ^ QtCore.Qt.AlignBottom,
            # offset_y = 0.1,
            font_size = 0.05,
            text_color = (0,0,0),
        )
        vp.overlays.append(overlay)

    vp.zoom_all()
    for t in node.output.particle_properties.particle_type.type_list:
        t.radius = args.particle_size
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    for i in range(len(args.custom_range)):
        if args.custom_range[i] < 0:
            args.custom_range[i] += node.source.num_frames
    if args.output_ext in MOVIE_TYPES:
        range_opt = RenderSettings.Range.CUSTOM_INTERVAL
    elif args.output_ext in IMAGE_TYPES:
        dataset.anim.current_frame = args.custom_range[0]
        range_opt = RenderSettings.Range.CURRENT_FRAME
    settings = RenderSettings(
        filename=args.output_file,
        size=args.dimensions,
        range=range_opt,
        custom_range=args.custom_range,
        renderer=renderer,
    )
    if args.output_ext in MOVIE_TYPES:
        settings.everyNthFrame = args.every_nth_frame
    vp.render(settings)


def add_output_path(args):
    args.input_file = os.path.abspath(args.input_file)
    input_ext = args.input_file.split('.')[-1]
    if args.output_file is None:
        args.output_file = (
            args.input_file
            .replace('.' + input_ext, '.' + args.output_ext)
        )
        if args.move_to_processed:
            args.output_file = args.output_file.replace('/raw/', '/processed/')
    else:
        args.output_file = os.path.abspath(args.output_file)
        args.output_ext = args.output_file.split('.')[-1]
        if args.output_ext not in ALL_OUTPUT_TYPES:
            raise ValueError(
                ".{} is not a valid output extension.\n".format(args.output_ext)
                + "Accepted extensions: {}".format(ALL_OUTPUT_TYPES)
            )

def add_custom_range(args):
    if args.custom_range is None:
        if args.output_ext in MOVIE_TYPES:
            args.custom_range = [0, -1]
        elif args.output_ext in IMAGE_TYPES:
            args.custom_range = [-1, -1]
    else:
        if len(args.custom_range) == 1:
            args.custom_range = [args.custom_range[0], args.custom_range[0]]
        if len(args.custom_range) > 2:
            raise ValueError("--custom-range takes 1 or 2 arguments only")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Render images or movies from trajectory file"
    )
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str, nargs='?', default=None)
    parser.add_argument('-d', '--dimensions', type=int, nargs=2,
                        default=[800, 600])
    parser.add_argument('-e', '--every-nth-frame', type=int, default=1)
    parser.add_argument('-f', '--frames-per-second', type=int, default=None)
    parser.add_argument('-m', '--move-to-processed', action='store_true',
                        default=False)
    parser.add_argument('-n', '--overlay-frame-num', action='store_true',
                        default=True)
    parser.add_argument('-o', '--output-ext', type=str, default='gif',
                        choices=ALL_OUTPUT_TYPES)
    parser.add_argument('-p', '--particle-size', type=float, default=0.5)
    parser.add_argument('-P', '--viewport', type=int, choices=[0, 1, 2, 3],
                        default=0)
    parser.add_argument('-r', '--renderer', choices=['opengl', 'tachyon'],
                        default='opengl')
    parser.add_argument('-R', '--custom-range', type=int, nargs='+', default=None)
    parser.add_argument('-s', '--same-dir', action='store_true', default=True)
    parser.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2],
                        default=2)
    args = parser.parse_args()
    add_output_path(args)
    add_custom_range(args)

    main(args)

