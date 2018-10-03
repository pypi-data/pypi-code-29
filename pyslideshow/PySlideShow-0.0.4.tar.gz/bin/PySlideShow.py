#!/usr/bin/env python

from PySlideShow import *
import argparse
import pygame
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(description='Configurable slide shows.')
parser.add_argument('slideshow', help='JSON file defining a Slideshow (e.g. Examples/slideshow.json)')
parser.add_argument('--fullscreen',
    action='store_true',
    help='Run slideshow in fullscreen mode' )
parser.add_argument('--minimal',
    action='store_true',
    help='Run in very small window to work on configuration of slideshow' )
args = parser.parse_args()

config = ConfigurationHandler(args.slideshow)
rendering = Rendering(args.fullscreen, args.minimal)
sequencer = SlideSequencer(rendering.getDisplay(), config.get_slide_list())

# rendering loop
sequencer.start()
while True:
    key = rendering.runA()
    if key == pygame.K_ESCAPE:
        break
    elif key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_CTRL:
        sequencer.forward(10)
    elif key == pygame.K_RIGHT:
        sequencer.forward(1)
    elif key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_CTRL:
        sequencer.backward(10)
    elif key == pygame.K_LEFT:
        sequencer.backward(1)
    elif key == pygame.K_SPACE:
        sequencer.set_paused(not sequencer.get_paused())
        if sequencer.get_paused():
            print 'Automatic transitions paused.'
        else:
            print 'Automatic transitions resumed.'

    if not sequencer.run():
        break

    rendering.runB()
