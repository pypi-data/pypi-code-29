import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys
import os

class AnchorSet:
    bottom_left = None
    bottom_right = None
    top_right = None
    top_left = None

    def __init__(self):
        pass


class Slide:
    slide_index = None
    fn = ''
    display = None
    dry = False

    duration = 4
    appearanceTime = None
    normalizedTime = None
    anchor_begin = AnchorSet()
    anchor_end = AnchorSet()

    def __init__(self, slide_index, configuration, display, configuration_directory):
        self.slide_index = slide_index
        self.fn = configuration['file']
        self.display = display
        if not self.dry:
            print "Loading image '%s' ..." % self.fn
            self.load_texture(os.path.join(configuration_directory, self.fn))
            self.parseConfirguration(configuration)

    def set_anchor(self, anchor_configuration):

        # set implicit default parameters
        if not 'zoom' in anchor_configuration.keys():
            anchor_configuration['zoom'] = 1
        if not 'position' in anchor_configuration.keys():
            anchor_configuration['position'] = 'top_left'
        if not 'offset_x' in anchor_configuration.keys():
            anchor_configuration['offset_x'] = 'top_left'

        anchor = AnchorSet()
        obj_width = self.base_scale * self.txt_width * anchor_configuration['zoom']
        obj_height = self.base_scale * self.txt_height * anchor_configuration['zoom']
        if anchor_configuration['position'] == 'top_left':
            anchor.bottom_left  = np.array((0, self.display_height - obj_height))
            anchor.bottom_right = np.array((obj_width, self.display_height - obj_height))
            anchor.top_right    = np.array((obj_width, self.display_height))
            anchor.top_left     = np.array((0, self.display_height))
        elif anchor_configuration['position'] == 'top_right':
            anchor.bottom_left  = np.array((self.display_width - obj_width, self.display_height - obj_height))
            anchor.bottom_right = np.array((self.display_width, self.display_height - obj_height))
            anchor.top_right    = np.array((self.display_width, self.display_height))
            anchor.top_left     = np.array((self.display_width - obj_width, self.display_height))
        elif anchor_configuration['position'] == 'bottom_left':
            anchor.bottom_left = np.array((0, 0))
            anchor.bottom_right = np.array((obj_width, 0))
            anchor.top_right = np.array((obj_width, obj_height))
            anchor.top_left = np.array((0, obj_height))
        else:
            print "Configuration Error Slide %d: Position '%s' not supported." % (self.slide_index, anchor_configuration['position'])
            sys.exit(1)
        return anchor

    def parseConfirguration(self, configuration):
        '''
            Read configuration and especially its animation part
            and generate the parameters for the plave vertices and
            texture coordinates in the beinning and the end of the
            slide from it. The slide will then interpolate between
            them to do the animation.

            Coordinates are defined with respect to the OpenGL coordiante
            frame, which has its origin at the bottom left
        '''

        if not 'begin' in configuration.keys():
            configuration['begin'] = dict()
        if not 'end' in configuration.keys():
            configuration['end'] = dict()

        self.anchor_begin = self.set_anchor(configuration['begin'])
        self.anchor_end = self.set_anchor(configuration['end'])
        pass

    def load_texture(self, fn):
        textureSurface = pygame.image.load(fn)
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()

        # scale quad to have the smaller die filling the screen
        self.txt_width = float(width)
        self.txt_height = float(height)
        self.display_width = float(self.display[0])
        self.display_height = float(self.display[1])
        scale_width = self.display_width / self.txt_width
        scale_height = self.display_height / self.txt_height
        self.base_scale = max(scale_width, scale_height)

        glEnable(GL_TEXTURE_2D)
        self.texid = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                   0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    def render(self, opacity):

        if self.dry:
            return

        # cropped zoom increases size while not changing the covered screen area
        cropped_zoom = 1
        cropped_zoom_range = 1. / cropped_zoom
        cropped_zoom_offset_x = 0.0
        cropped_zoom_offset_y = 0.0

        # linear interpolation between keyframes
        alpha = (1.0 - self.normalizedTime)
        beta = self.normalizedTime
        bottom_left = alpha * self.anchor_begin.bottom_left + beta * self.anchor_end.bottom_left
        bottom_right = alpha * self.anchor_begin.bottom_right + beta * self.anchor_end.bottom_right
        top_right = alpha * self.anchor_begin.top_right + beta * self.anchor_end.top_right
        top_left = alpha * self.anchor_begin.top_left + beta * self.anchor_end.top_left

        glBlendFunc(GL_CONSTANT_ALPHA, GL_ONE_MINUS_CONSTANT_ALPHA)
        glBlendEquation(GL_FUNC_ADD)
        glBlendColor(1.0, 1.0, 1.0, opacity)

        glBindTexture(GL_TEXTURE_2D, self.texid)
        glBegin(GL_QUADS)

        # bottom-left
        glTexCoord2f(cropped_zoom_offset_x, cropped_zoom_offset_y)
        glVertex3f(bottom_left[0], bottom_left[1], 0)

        # bottom-right
        glTexCoord2f(cropped_zoom_offset_x + cropped_zoom_range, cropped_zoom_offset_y)
        glVertex3f(bottom_right[0], bottom_right[1], 0)

        # top-right
        glTexCoord2f(cropped_zoom_offset_x + cropped_zoom_range, cropped_zoom_offset_y + cropped_zoom_range)
        glVertex3f(top_right[0], top_right[1], 0)

        # top-left
        glTexCoord2f(cropped_zoom_offset_x, cropped_zoom_offset_y + cropped_zoom_range)
        glVertex3f(top_left[0], top_left[1], 0)

        glEnd()
