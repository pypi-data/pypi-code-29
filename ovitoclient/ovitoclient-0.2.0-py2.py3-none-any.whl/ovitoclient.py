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
    if args.output_ext == '.gif' and args.frames_per_second is not None:
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
    for i in range(2):
        if args.custom_range[i] < 0:
            args.custom_range[i] += node.source.num_frames + 1
    settings = RenderSettings(
        filename=args.output_file,
        size=args.dimensions,
        renderer=renderer,
        custom_range=args.custom_range
    )
    if args.output_ext == '.gif':
        settings.range = RenderSettings.Range.CUSTOM_INTERVAL
        settings.everyNthFrame = args.every_nth_frame
    vp.render(settings)


def add_output_path(args):
    args.input_file = os.path.abspath(args.input_file)
    input_ext = '.' + args.input_file.split('.')[-1]
    if args.output_file is None:
        args.output_file = (
            args.input_file
            .replace(input_ext, args.output_ext)
        )
        if not args.same_dir:
            args.output_file = args.output_file.replace('/raw/', '/processed/')
    else:
        args.output_file = os.path.abspath(args.output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Render GIF from lammpstrj file")
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str, nargs='?', default=None)
    parser.add_argument('-d', '--dimensions', type=int, nargs=2,
                        default=[800,600])
    parser.add_argument('-e', '--every-nth-frame', type=int, default=1)
    parser.add_argument('-f', '--frames-per-second', type=int, default=None)
    parser.add_argument('-o', '--output-ext', type=str, default='.gif')
    parser.add_argument('-p', '--particle-size', type=float, default=0.5)
    parser.add_argument('-r', '--renderer', choices={'opengl', 'tachyon'},
                        default='opengl')
    parser.add_argument('-s', '--same-dir', action='store_true', default=False)
    parser.add_argument('-v', '--verbosity', type=int, choices={0, 1, 2},
                        default=2)
    parser.add_argument('-n', '--overlay-frame-num', action='store_true',
                        default=True)
    parser.add_argument('-R', '--custom-range', type=int, nargs=2,
                        default=[0, -1])
    parser.add_argument('-P', '--viewport', type=int, choices = {0, 1, 2, 3},
                        default=0)
    args = parser.parse_args()
    add_output_path(args)

    main(args)

