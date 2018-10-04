#!/usr/bin/env python
"""Exposes Matplotlib's colormaps so they can be used (for example) with OpenCV."""

import matplotlib.cm
import numpy as np

# This colormap list code has been adapted from:
# https://matplotlib.org/tutorials/colors/colormaps.html
# It is useful to have colormaps grouped by categories.
cmaps_groups = [
    {'group': 'Perceptually Uniform Sequential',
    'colormaps': [
        'viridis', 'plasma', 'inferno', 'magma', 'cividis']},

    {'group':  'Sequential',
    'colormaps': [
        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']},

    {'group': 'Sequential (2)',
    'colormaps': [
        'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
        'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
        'hot', 'afmhot', 'gist_heat', 'copper']},

    {'group': 'Diverging',
    'colormaps': [
        'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']},

    {'group': 'Qualitative',
    'colormaps': ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                  'Dark2', 'Set1', 'Set2', 'Set3',
                  'tab10', 'tab20', 'tab20b', 'tab20c']},

    {'group':  'Miscellaneous',
    'colormaps': [
        'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
        'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
        'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']}]

# Add the _r versions (reverse colormaps).
for group_data in cmaps_groups:
    group_data['colormaps'] += [s + '_r' for s in group_data['colormaps']]


def cmap(cmap_name):
    """Extract colormap color information as a LUT
    compatible with cv2.applyColormap()."""

    c_map = matplotlib.cm.get_cmap(cmap_name, 256)
    rgba_data = matplotlib.cm.ScalarMappable(cmap=c_map).to_rgba(np.arange(0, 1.0, 1.0 / 256.0), bytes=True)
    rgba_data = rgba_data[:, 0:-1].reshape((256, 1, 3))

    # Convert to BGR, uint8, for OpenCV.
    cmap = np.zeros((256, 1, 3), np.uint8)
    cmap[:, :, :] = rgba_data[:, :, ::-1]

    return cmap
