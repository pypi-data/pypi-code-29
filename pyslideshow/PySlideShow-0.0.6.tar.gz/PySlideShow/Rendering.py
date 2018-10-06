import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
import time


class Rendering:
    targetFps = 60
    targetTime = float(1) / targetFps

    lastFrameTime = None
    aveRenderTime = None
    frameCounter = None
    display = None

    def __init__(self, enableFullscreen = False, enableMinimal = False):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption('PySlide - V0.8')

        # default is to select largest available resolution
        self.display = pygame.display.list_modes()[0]

        if enableMinimal:
            s = 400
            self.display = (s,s*9/16)

        mode = pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT
        if enableFullscreen:
            mode = mode | pygame.FULLSCREEN
        screen = pygame.display.set_mode(
            self.display, mode)

        # perspective mode - might be re-used in future for multi layer perspective effects
        #gluPerspective(45, float(self.display[0]) / float(self.display[1]), 0.1, 50.0)
        #glTranslatef(0.0, 0.0, -2.4)

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(0.0, float(self.display[0]), 0.0, float(self.display[1]), -10.0, 10.0)

        glEnable(GL_BLEND)

        self.lastFrameTime = time.time()
        self.aveRenderTime = self.targetTime
        self.frameCounter = 0

    def getDisplay(self):
        return self.display

    def runA(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def runB(self):
        pygame.display.flip()

        # measure how long to wait to reach target framerate
        timeDelta = time.time() - self.lastFrameTime
        self.aveRenderTime = 0.1 * timeDelta + 0.9 * self.aveRenderTime
        needToWait = 0.8 * max(0, self.targetTime - timeDelta)
        time.sleep(needToWait)

        if self.frameCounter > 200:
            print "time=%.2f ms (limit %.2f ms)" % ((self.aveRenderTime * 1000), (self.targetTime * 1000))
            self.frameCounter = 0
        self.frameCounter = self.frameCounter + 1

        # measure resulting framerate
        timeDelta = time.time() - self.lastFrameTime
        self.lastFrameTime = time.time()
        fps = float(1) / timeDelta

        #if fps < self.targetFps:
        #    print 'Error: Framerate too low - %d fps while target is %d fps' % (fps, self.targetFps)


