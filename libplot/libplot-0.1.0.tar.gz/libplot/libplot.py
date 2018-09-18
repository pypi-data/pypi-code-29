#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:15:07 2018

@author: antony
"""
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ALPHA = 0.8
MARKER_SIZE = 10

TRANS_GRAY = (0.5, 0.5, 0.5, 0.5)

BLUES = sns.color_palette('Blues', 8)[2:]
GREENS = sns.color_palette('Greens', 8)[2:]


def setup():
  fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf' #fontpath = '/ifs/scratch/cancer/Lab_RDF/abh2138/scRNA/analysis/Arial.ttf'
  prop = matplotlib.font_manager.FontProperties(fname=fontpath)
  
  matplotlib.rcParams['axes.unicode_minus'] = False
  matplotlib.rcParams['font.family'] = prop.get_name()
  matplotlib.rcParams['font.size'] = 14 
  matplotlib.rcParams['mathtext.default'] = 'regular'
  
  sns.set(font="Arial")
  sns.axes_style({'font.family': ['sans-serif'], 'font.sans-serif': ['Arial']})
  sns.set_style("white")
  sns.set_style("ticks")
  sns.set_style({"axes.facecolor": 'none'})


def new_ax(fig, *args, **kwargs):
    zorder = kwargs.get('zorder', 1)
    
    if len(args) == 3:
        ax = fig.add_subplot(args[0], args[1], args[2], zorder=zorder)
    else:
        subplot = kwargs.get('subplot', '111')
        
        if type(subplot) is tuple:
            ax = fig.add_subplot(subplot[0], subplot[1], subplot[2], zorder=zorder)
        else:
            ax = fig.add_subplot(subplot, zorder=zorder)
  
    format_axes(ax)
    
    return ax

def new_base_fig(w=8, h=8):
    fig = plt.figure(figsize=[w, h])
    
    return fig

def new_fig(w=8, h=8, subplot=111):
    fig = new_base_fig(w, h)
    
    ax = new_ax(fig, subplot)
  
    format_axes(ax)
    
    return fig, ax

def grid_size(n):
    return int(np.ceil(np.sqrt(n)))

def polar_fig(w=5, h=5, subplot=111):
    fig = plt.figure(figsize=[w, h])
    #ax = fig.add_subplot(subplot, polar=True)
    return fig

def polar_ax(fig, subplot=111):
    if type(subplot) is tuple:
        ax = fig.add_subplot(subplot[0], subplot[1], subplot[2], polar=True)
    else:
        ax = fig.add_subplot(subplot, polar=True)
    
    return ax

def polar_clock_ax(fig, subplot=111):
    ax = polar_ax(fig, subplot)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rgrids([], labels=[])
    ax.set_yticklabels([])
    # Set the grid lines at 0 6 radii
    lines, labels = plt.thetagrids(range(0, 360, 60), list(range(0, 6)))
    ax.tick_params(pad=0.5)
    return ax



def savefig(fig, out, pad=2, dpi=300):
  fig.tight_layout(pad=pad) #rect=[o, o, w, w])
  plt.savefig(out, dpi=dpi)
  

def base_boxplot(df, x_label=None, y_label=None, hue=None, width=0.1, color=BLUES[0], linewidth=1.5, fliersize=2, orient='v', ax=None):
    if ax is None:
        fig, ax = new_fig()
      
    sns.boxplot(x=x_label, y=y_label, hue=hue, data=df, width=width, fliersize=fliersize, color=color, linewidth=linewidth, orient="v", saturation=1, ax=ax)
          
    for i in range(0, len(ax.lines)):
        line = ax.lines[i]
        #c = colors[i // 6]
        line.set_color(color)
        line.set_mfc(color)
        line.set_mec(color)
        line.set_solid_capstyle('butt')
        
        # Change the outlier style
        if i % 6 == 5:
            line.set_marker('o')
      
        for i in range(4, len(ax.lines), 6):      
            ax.lines[i].set_color('white')
      
        for i in range(0, len(ax.artists)):
            ax.artists[i].set_facecolor(color)
            ax.artists[i].set_edgecolor(color)
            
    return ax


def boxplot(df, x_label=None, y_label=None, hue=None, width=0.1, color=BLUES[0], linewidth=1.5, fliersize=2, orient='v', ax=None):
    ax = base_boxplot(x_label=x_label, y_label=y_label, hue=hue, df=df, width=width, color=color, linewidth=linewidth, fliersize=fliersize, orient=orient, ax=ax)
      
    format_axes(ax)
      
    return ax



def base_violinplot(df, x_label=None, y_label=None, hue=None, width=0.4, color=BLUES[0], ax=None):
    if ax is None:
        fig, ax = new_fig()
    
    sns.violinplot(x=x_label, y=y_label, hue=hue, data=df, width=width, color=tint(color, 0.5), linewidth=0, orient="v", saturation=1, ax=ax)
      
    format_axes(ax)
      
    return ax

def violinplot(df, x_label=None, y_label=None, hue=None, width=0.4, color=BLUES[0], ax=None):
    ax = base_violinplot(df, x_label=x_label, y_label=y_label, hue=hue, width=width, color=color, ax=ax)
      
    format_axes(ax)
      
    return ax


def scatter(x, y, s=MARKER_SIZE, c=None, cmap=None, norm=None, alpha=ALPHA, marker='o', fig=None, ax=None, label=None):
    if ax is None:
        fig, ax = new_fig()
        
    ax.scatter(x, y, s=s, color=c, cmap=cmap, norm=norm, marker=marker, alpha=alpha, label=label)
    
    return fig, ax


def correlation_plot(x, y, marker='o', s=MARKER_SIZE, c=None, cmap=None, norm=None, alpha=ALPHA, xlabel=None, ylabel=None, x1=None, x2=None, fig=None, ax=None):
    if ax is None:
        fig, ax = new_fig()
         
    ax.scatter(x, y, c=c, cmap=cmap, norm=norm, s=s, marker=marker, alpha=alpha)
    
    sns.regplot(x, y, ax=ax, scatter=False)
    
    if xlabel is not None:
        ax.set_xlabel(xlabel)
        
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    
    #if cmap is not None:
    #    add_colorbar(fig, cmap, x1=None, x2=None, norm=norm)
    
    return fig, ax


def plot(x, y, s=MARKER_SIZE, c=None, alpha=ALPHA, fig=None, ax=None, label=''):
    if ax is None:
        fig, ax = new_fig()
        
    gcf = ax.plot(x, y, c=c, alpha=alpha, label=label)
    
    return fig, ax, gcf


def invisible_axes(ax):
    """
    Make axes invisible.
    
    Parameters
    ----------
    ax :
        Matplotlib ax object.
    """
    
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
  

def format_axes(ax, x='', y=''):
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.minorticks_on()
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    ax.get_xaxis().set_tick_params(which='both', direction='in')


def add_colorbar(fig, cmap, x1=None, x2=None, norm=None):
    cax = fig.add_axes([0.8, 0.1, 0.15, 0.02])
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, ticks=[0, 1.0], orientation='horizontal')
    
    if x1 is None:
        if norm is not None:
            x1 = norm.vmin
        else:
            x1 = 0
            
    if x2 is None:
        if norm is not None:
            x2 = norm.vmax
        else:
            x2 = 1
    
    cb.set_ticklabels([x1, x2])
    cb.outline.set_linewidth(0.1)
    cb.ax.tick_params(width=0.1, length=0)


def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.sqrt(x**2 + y**2)
    return (theta, rho)


def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return (x, y)


def tint(color, t):
    r = max(0, min(1, (color[0] + (1 - color[0]) * t)))
    g = max(0, min(1, (color[1] + (1 - color[1]) * t)))
    b = max(0, min(1, (color[2] + (1 - color[2]) * t)))
    
    return (r, g, b)