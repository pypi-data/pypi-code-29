import numpy as np

def circle(x0,y0,r,theta):
    return x0+r*np.cos(theta), y0+r*np.sin(theta)

def ellipse(x0,y0,ax_x,ax_y,theta):
    return x0+ax_x*np.cos(theta), y0+ax_y*np.sin(theta)
