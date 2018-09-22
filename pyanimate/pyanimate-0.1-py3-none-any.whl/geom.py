import cairo
from PIL import Image
import numpy as np
import math


def make_cairo_frames(size, count, draw):
    for i in range(count):
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, size[0], size[1])
        ctx = cairo.Context(surface)
        ctx.rectangle(0, 0, size[0], size[1])
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()
        draw(ctx, size, count, i)
        surface.write_to_png('__make_cairo_frames__.png')
        img = Image.open('__make_cairo_frames__.png')
        frame = np.array(img)
        yield(frame)

def draw_point(ctx, pos, size, color=(0, 0, 0)):
    ctx.arc(pos[0], pos[1], size, 0, 2*math.pi)
    ctx.set_source_rgb(*color)
    ctx.fill()


#
# Draw a tick on a the line ab
#
# Draws a line half way along the line ab, at right angles
# to it.
#
# ctx - pycairo context
# a - (x, y) tuple point a
# b - (x, y) tuple point b
# size - length of tick
def draw_tick(ctx, a, b, size, count=1):
    a = np.asarray(a)
    b = np.asarray(b)
    c = (a + b)/2
    c_step = c*size/np.linalg.norm(c)
    ang = math.atan2(b[1]-a[1], b[0]-a[0]) + math.pi/2

    for i in range(count):
        pos = c + c_step*i
        d = pos[0]+size*math.cos(ang), pos[1]+size*math.sin(ang)
        e = pos[0]-size*math.cos(ang), pos[1]-size*math.sin(ang)
        ctx.move_to(*d)
        ctx.line_to(*e)
    
