import cairo
import numpy as np
import math

class Axes:
    def __init__(self, pixel_size, start, extent):
        self.pixel_size = pixel_size
        self.start = start
        self.extent = extent

    def axes_to_pixel(self, pos):
        px = (pos[0] - self.start[0])*self.pixel_size[0]/self.extent[0]
        py = self.pixel_size[1]-(pos[1] - self.start[1])*self.pixel_size[1]/self.extent[1]
        return px, py

    def pixel_length(self, x):
        return x*self.pixel_size[0]/self.extent[0]

    def draw_axes(self, ctx, div=(1, 1)):
        for p in self.get_divs(self.pixel_size[0], self.start[0], self.extent[0], div[0]):
            ctx.move_to(*self.axes_to_pixel((p, self.start[1])))
            ctx.line_to(*self.axes_to_pixel((p, self.start[1]+self.extent[1])))
        for p in self.get_divs(self.pixel_size[1], self.start[1], self.extent[1], div[1]):
            ctx.move_to(*self.axes_to_pixel((self.start[0], p)))
            ctx.line_to(*self.axes_to_pixel((self.start[0]+self.extent[0], p)))
        ctx.set_source_rgb(.5, .5, 1)
        ctx.set_line_width(2)
        ctx.stroke()

        ctx.set_source_rgb(0.1, 0.1, 0.1)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(15)
        for p in self.get_divs(self.pixel_size[0], self.start[0], self.extent[0], div[0]):
            if abs(p)>0.001:
                pstr = str(round(p*1000)/1000)
                ppx = self.axes_to_pixel((p, 0))
                x, y, width, height, dx, dy = ctx.text_extents(pstr)
                ctx.move_to(ppx[0]-width-4, ppx[1]+height+4)
                ctx.show_text(pstr)
        for p in self.get_divs(self.pixel_size[1], self.start[1], self.extent[1], div[1]):
            if abs(p)>0.001:
                pstr = str(round(p*1000)/1000)
                ppx = self.axes_to_pixel((0, p))
                x, y, width, height, dx, dy = ctx.text_extents(pstr)
                ctx.move_to(ppx[0]-width-4, ppx[1]+height+4)
                ctx.show_text(pstr)

        ctx.move_to(*self.axes_to_pixel((self.start[0], 0)))
        ctx.line_to(*self.axes_to_pixel((self.start[0]+self.extent[0], 0)))
        ctx.move_to(*self.axes_to_pixel((0, self.start[1])))
        ctx.line_to(*self.axes_to_pixel((0, self.start[1]+self.extent[1])))
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.stroke()
        p = self.axes_to_pixel((0, 0))
        ctx.arc(p[0], p[1], 8, 0, 2*math.pi)
        ctx.stroke()

    def get_divs(self, pixel_size, start, extent, div):
        divs = []
        n = math.ceil(start/div)*div
        while n <= start + extent:
            divs.append(n)
            n += div
        return divs

def plot_curve(ctx, fn, axes, color=(1, 0, 0), extent=None, lw=3):
    points = []
    for x in np.linspace(axes.start[0], axes.start[0]+axes.extent[0], 100):
        if not extent or extent[0] < x < extent[1]:
            points.append((x, fn(x)))
    if points:
        ctx.move_to(*axes.axes_to_pixel(points[0]))
        for p in points[1:]:
            ctx.line_to(*axes.axes_to_pixel(p))
    ctx.set_source_rgb(*color)
    ctx.set_line_width(lw)
    ctx.stroke()
 

def plot_yx_curve(ctx, fn, axes, color=(1, 0, 0), extent=None, lw=3):
    points = []
    for y in np.linspace(axes.start[1], axes.start[1]+axes.extent[1], 100):
        if not extent or extent[0] < y < extent[1]:
            points.append((fn(y), y))
    if points:
        ctx.move_to(*axes.axes_to_pixel(points[0]))
        for p in points[1:]:
            ctx.line_to(*axes.axes_to_pixel(p))
    ctx.set_source_rgb(*color)
    ctx.set_line_width(lw)
    ctx.stroke()
 

def attribution(ctx, size, text, color=(0.5, 0, 0)):
    ctx.set_source_rgb(*color)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(20)
    x, y, width, height, dx, dy = ctx.text_extents(text)
    ctx.move_to(size[0]-width-4, size[1]-4)
    ctx.show_text(text)
