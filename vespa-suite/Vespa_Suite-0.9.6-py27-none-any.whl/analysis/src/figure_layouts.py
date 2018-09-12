# Python modules
from __future__ import division
import argparse
import os
import sys
import platform
import imp
import xml.etree.cElementTree as ElementTree

# 3rd party modules
import matplotlib as mpl
mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.table as mtable
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, NullFormatter, MaxNLocator,\
    AutoMinorLocator

from matplotlib.backends import pylab_setup
_backend_mod, new_figure_manager, draw_if_interactive, _show = pylab_setup()

# Our modules
import util_import
import figure_layouts

import vespa.common.util.ppm as util_ppm
import vespa.common.util.misc as util_misc
import vespa.common.util.time_ as util_time

from vespa.common.constants import DEGREES_TO_RADIANS as DTOR

DESC =  \
"""Blah blah blah blah blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah blah blah blah blah .

Blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah .
 
"""



def lcm_like(dataset,   viffpath='', 
                        vespa_version='',
                        timestamp='',
                        fontname='Courier New',
                        minplot=0.1,
                        maxplot=4.9,
                        nobase=False,
                        extfig=None,
                        fixphase=False,
                        verbose=False, debug=False):
    """
    Some typical save type formats = 'svg' 'eps' 'pdf' 'png' 'raw' 'rgba' 'ps' 'pgf' etc.
    Typical fontnames  'Consolas' 'Calibri' 'Courier New' 'Times New Roman'
    
    minplot and maxplot are in PPM
    
    """
    # Print Control Setting ----------------------

    if viffpath:
        viffname = os.path.basename(viffpath)
    else:
        viffname = 'none'

    if vespa_version == '':
        vespa_version = util_misc.get_vespa_version() + ' (runtime)'
        
    if timestamp == '':
        timestamp = util_time.now().isoformat()
        
    data_source = os.path.basename(dataset.blocks["raw"].get_data_source(dataset.all_voxels[0]))
    dim0, dim1, dim2, dim3 = dataset.spectral_dims
    voxel = dataset.all_voxels

    # Process 'fit' block to get results --------------------------------------

    key = 'fit'
    if key in dataset.blocks.keys():
        block = dataset.blocks[key]
        results = block.chain.run(voxel, entry='output_refresh')

        lw    = results['fitted_lw']
        lwmin = results['minmaxlw'][0]
        lwmax = results['minmaxlw'][1]
        fit_data, nsect = dataset.blocks['fit'].results_in_table(voxel[0], lw=lw, 
                                                                           lwmin=lwmin, 
                                                                           lwmax=lwmax, 
                                                                           fixphase=fixphase,
                                                                           nozeros=True,
                                                                           noppm=True)
        nfitcol = len(fit_data[0])  
    else:
        msg = r"This dataset has no 'fit' block, returning." 
        raise ValueError(msg)

    # Gather Data -------------------------------------------------------------

    freq  = results['data'].copy() 
    base  = results['fit_baseline'].copy() 
    yfit  = results['yfit'].copy() 
    yfits = results['yfit'].copy() if len(yfit.shape)==1 else np.sum(yfit, axis=0) 
    if len(yfit.shape) == 1:
        yfit.shape = 1,yfit.shape[0]

    if fixphase:
        x,y,z = voxel[0]
        ph0  = -block.fit_results[-2,x,y,z]
        ph1  = -block.fit_results[-1,x,y,z]
        piv  = (dim0/2.0) - (dataset.frequency*(dataset.phase_1_pivot - dataset.resppm)/(dataset.sw/dim0))
        arr1 = (np.arange(dim0) - piv)/dim0
        ph0  = ph0 * DTOR
        ph1  = ph1 * DTOR * arr1
        phase  = np.exp(1j * (ph0 + ph1))
        freq  *= phase
        base  *= phase
        yfits *= phase


    # Calculate full xaxis values
    xvals = [util_ppm.pts2ppm(val, dataset) for val in range(dim0)]
    minppm, maxppm = xvals[-1], xvals[0]

    # Calculate xaxis range to plot, create tics
    minplot = minplot if minplot >= minppm else minppm
    maxplot = maxplot if maxplot <= maxppm else maxppm
    imin = int(util_ppm.ppm2pts(maxplot, dataset))
    imax = int(util_ppm.ppm2pts(minplot, dataset))
    tmin = np.round((minplot+0.5))                  # integer ppm just above minppm
    tmax = np.round((maxplot-0.5))                  # integer ppm just under maxppm
    xtick_range = np.arange(tmin, tmax+1, 1.0)
    xvals = xvals[imin:imax]                        # trim to plot width

    # Create the figure
    if extfig is None:
        fig = plt.figure(figsize=(11,8.5), facecolor='white')
    else:
        fig = extfig
        
    plt.subplots_adjust(hspace=0.001)
    nullfmt = NullFormatter()                   # used to suppress labels on an axis
    local_grey = (10./255.,10./255.,10./255.)   # used to tweak font color locally

    # Layout for an LCModel-like landscape report

    left, bottom    = 0.05, 0.07        # set up for 8.5x11 landscape printout
    w1, w2          = 0.55, 0.35
    h1, h2          = 0.71, 0.07
    hpad, vpad      = 0.02, 0.001    
    
    rect1 = [left,         bottom+h1, w1, h2]    # xmin, ymin, dx, and dy 
    rect2 = [left,         bottom,    w1, h1]
    rect4 = [left+w1+hpad, bottom, w2, h1+h2+0.015]

    # Noise Residual Plot -----------------------------------------------------
    
    dat1 = (freq - yfits - base)[imin:imax].real
    min1, max1 = min(dat1),max(dat1)
    delt1 = (max1 - min1)*0.75
    min1, max1 = min1 - delt1, max1 + delt1
    
    ax1 = fig.add_axes(rect1)               
    ax1.xaxis.set_major_formatter(nullfmt)  # no x labels, have to go before plot()
    ax1.plot(xvals, dat1, 'k')
    ax1.set_xlim(maxplot, minplot)
    ax1.set_ylim(min1, max1)
    ax1.set_xticks(xtick_range)
    ax1.set_yticks([0.0, max1])
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))

    # Data, Fit, Baseline Plot ------------------------------------------------

    dat2  = freq[imin:imax].real
    dat2b = (yfits+base)[imin:imax].real
    dat2c = base[imin:imax].real
    min2, max2 = min(dat2),max(dat2)
    delt2 = (max2 - min2)*0.05
    min2, max2 = min2-delt2, max2+delt2
    tmp = abs(max2) if abs(max2) > abs(min2) else abs(min2)     # in case spectrum flipped
    major2 = tmp/4.0
    if major2 > 2.5: 
        major2 = np.round(major2,0)

    ax2 = fig.add_axes(rect2)              
    ax2.plot(xvals, dat2,  'k')
    ax2.plot(xvals, dat2b, 'r', alpha=0.7)
    if not nobase:
        ax2.plot(xvals, dat2c, 'g')
    ax2.set_ylabel('Spectral Data, Fit, Baseline', fontsize=8.0)
    ax2.set_xlabel('Chemical Shift [ppm]',         fontsize=8.0)
    ax2.set_ylim(min2, max2)
    ax2.set_xlim(maxplot, minplot)
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax2.yaxis.set_major_locator(MultipleLocator(major2))        # this is for even distrib across plot
    ax2.yaxis.set_minor_locator(MultipleLocator(major2*0.5))
    # TODO bjs - from brp512 layout
    # ax0.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    # ax0.yaxis.set_minor_locator(AutoMinorLocator(2))
    
    # Common Settings for both plot axes --------------------------------------
    
    for ax in [ax1,ax2]:
        ax.xaxis.set_major_locator(MultipleLocator(1))        # this is for even distrib across plot
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        ax.grid(which='major', axis='x', linewidth=0.50, linestyle='-', color='0.75')
        ax.grid(which='minor', axis='x', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='major', axis='y', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='minor', axis='y', linewidth=0.25, linestyle=':', color='0.75')        

    # Table Setup -------------------------------------------------------------

    ax4 = fig.add_axes(rect4)      
    ax4.xaxis.set_major_formatter(nullfmt)      # turn off axis markers
    ax4.yaxis.set_major_formatter(nullfmt)
    ax4.axis('off')

    the_table = ax4.table(cellText=fit_data, cellLoc='left',
                          colLoc='left',   colLabels=None, colWidths=None,
                          rowLoc='center', rowLabels=None,
                          fontsize=7.0, loc='upper center')
      
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(7.0)  
    for item in range(len(fit_data[0])):
        the_table.auto_set_column_width(item)   # mpl bug requires that each col be added individually
    
    table_props = the_table.properties()
    cheight = table_props['children'][0].get_height()   # all start with same default
    keys = table_props['celld'].keys()
    for key in keys:                            # use cell dict to test grid location for line settings
        cell = table_props['celld'][key]
        cell.set_height(1.0*cheight)
        cell.get_text().set_fontname(fontname)
        if key[0] in nsect:                     # this is a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'BLT'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'BRT'
            else:
                cell.visible_edges = u'BT'
            cell.set_linewidth(1.0)
            cell.set_linestyle('-')
            cell.get_text().set_fontweight('bold')
        else:                                   # not a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'L'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BL'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'R'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BR'
            else:
                cell.visible_edges = u''
                if key[0] == len(fit_data)-1:   # last line in table
                    cell.visible_edges = u'B'
            cell.set_linewidth(0.25)
            cell.set_linestyle('-')
    
    # Retrieve an element of a plot and set properties
    for tick in ax2.xaxis.get_ticklabels():
        tick.set_fontsize(8.0)
        tick.set_fontname(fontname)
        tick.set_color(local_grey)
        tick.set_weight('bold')         # 'normal'   

    for ax in [ax1,ax2]:
        ax.xaxis.label.set_fontname(fontname)
        ax.yaxis.label.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontsize(8.0)
        for tick in ax.yaxis.get_ticklabels():
            tick.set_fontsize(7.0)
            tick.set_fontname(fontname)
            tick.set_color(local_grey)
            tick.set_weight('bold')  
            if ax == ax2:
                tick.set_rotation(90)  

    if fixphase:
        msg = u"Vespa-Analysis Version: %s             'Fit' Tab Results  (Phase0/1 Corrected)               Processing Timestamp: %s" % (vespa_version, timestamp)
    else:
        msg = u"Vespa-Analysis Version: %s                 'Fit' Tab Results                                 Processing Timestamp: %s" % (vespa_version, timestamp)
    plt.figtext(0.03, 0.95, msg, 
                            wrap=True, 
                            horizontalalignment='left', 
                            fontsize=8, 
                            fontname=fontname)
    msg = u"VIFF File   : %s \nData Source : %s" % (viffname, data_source)
    plt.figtext(0.03, 0.90, msg, 
                            wrap=True, 
                            horizontalalignment='left',
                            color=local_grey, 
                            fontsize=10, 
                            fontname=fontname)

    
    fig.canvas.draw()
    
    return fig


def analysis_plot2(dataset, viffpath='', 
                            vespa_version='',
                            timestamp='',
                            fontname='Courier New',
                            minplot=0.1,
                            maxplot=4.9,
                            extfig=None,
                            nobase=False,
                            fixphase=False,
                            verbose=False, debug=False):
    """
    Some typical save type formats = 'svg' 'eps' 'pdf' 'png' 'raw' 'rgba' 'ps' 'pgf' etc.
    Typical fontnames  'Consolas' 'Calibri' 'Courier New' 'Times New Roman'
    
    minplot and maxplot are in PPM
    
    """
    # Print Control Setting ----------------------

    if viffpath:
        viffname = os.path.basename(viffpath)
    else:
        viffname = 'none'

    if vespa_version == '':
        vespa_version = util_misc.get_vespa_version() + ' (runtime)'
        
    if timestamp == '':
        timestamp = util_time.now().isoformat()
        
    data_source = os.path.basename(dataset.blocks["raw"].get_data_source(dataset.all_voxels[0]))
    dim0, dim1, dim2, dim3 = dataset.spectral_dims
    voxel = dataset.all_voxels

    # Process 'fit' block to get results --------------------------------------

    key = 'fit'
    if key in dataset.blocks.keys():
        block = dataset.blocks[key]
        results = block.chain.run(voxel, entry='output_refresh')

        lw    = results['fitted_lw']
        lwmin = results['minmaxlw'][0]
        lwmax = results['minmaxlw'][1]
        fit_data, nsect = dataset.blocks['fit'].results_in_table(voxel[0], lw=lw, 
                                                                           lwmin=lwmin, 
                                                                           lwmax=lwmax, 
                                                                           fixphase=fixphase,
                                                                           nozeros=False,
                                                                           noppm=False)
        nfitcol = len(fit_data[0])  
    else:
        msg = r"This dataset has no 'fit' block, returning." 
        raise ValueError(msg)

    # Gather Data -------------------------------------------------------------

    freq  = results['data'].copy() 
    base  = results['fit_baseline'].copy() 
    yfit  = results['yfit'].copy() 
    yfits = results['yfit'].copy() if len(yfit.shape)==1 else np.sum(yfit, axis=0) 
    if len(yfit.shape) == 1:
        yfit.shape = 1,yfit.shape[0]

    if fixphase:
        x,y,z = voxel[0]
        ph0  = -block.fit_results[-2,x,y,z]
        ph1  = -block.fit_results[-1,x,y,z]
        piv  = (dim0/2.0) - (dataset.frequency*(dataset.phase_1_pivot - dataset.resppm)/(dataset.sw/dim0))
        arr1 = (np.arange(dim0) - piv)/dim0
        ph0  = ph0 * DTOR
        ph1  = ph1 * DTOR * arr1
        phase  = np.exp(1j * (ph0 + ph1))
        freq  *= phase
        base  *= phase
        yfits *= phase


    # Calculate full xaxis values
    xvals = [util_ppm.pts2ppm(val, dataset) for val in range(dim0)]
    minppm, maxppm = xvals[-1], xvals[0]

    # Calculate xaxis range to plot, create tics
    minplot = minplot if minplot >= minppm else minppm
    maxplot = maxplot if maxplot <= maxppm else maxppm
    imin = int(util_ppm.ppm2pts(maxplot, dataset))
    imax = int(util_ppm.ppm2pts(minplot, dataset))
    tmin = np.round((minplot+0.5))                  # integer ppm just above minppm
    tmax = np.round((maxplot-0.5))                  # integer ppm just under maxppm
    xtick_range = np.arange(tmin, tmax+1, 1.0)
    xvals = xvals[imin:imax]                        # trim to plot width

    # Create the figure
    if extfig is None:
        fig = plt.figure(figsize=(11,8.5), facecolor='white')
    else:
        fig = extfig
        
    plt.subplots_adjust(hspace=0.001)
    nullfmt = NullFormatter()                   # used to suppress labels on an axis
    local_grey = (10./255.,10./255.,10./255.)   # used to tweak font color locally

    # Layout for an LCModel-like landscape report

    left, bottom    = 0.02, 0.07        # set up for 8.5x11 landscape printout
    w1, w2          = 0.45, 0.45
    h1, h2          = 0.40, 0.40
    hpad, vpad      = 0.04, 0.001    

    rect1 = [left+w1+hpad, bottom,    w2, h1]    # xmin, ymin, dx, and dy 
    rect2 = [left+w1+hpad, bottom+h1, w2, h1]
    rect4 = [left,         bottom,    w1, h1+h2+0.015]

    fsiz4 = 7.0

    # Data, Fit, Baseline Plot ------------------------------------------------

    dat2  = freq[imin:imax].real
    dat2b = (yfits+base)[imin:imax].real
    dat2c = base[imin:imax].real
    min2, max2 = min(dat2),max(dat2)
    delt2 = (max2 - min2)*0.05
    min2, max2 = min2-delt2, max2+delt2
    tmp = abs(max2) if abs(max2) > abs(min2) else abs(min2)     # in case spectrum flipped
    major2 = tmp/4.0
    if major2 > 2.5: 
        major2 = np.round(major2,0)

    ax2 = fig.add_axes(rect2)              
    ax2.xaxis.set_major_formatter(nullfmt)  # no x labels, have to go before plot()
    ax2.plot(xvals, dat2,  'k')
    ax2.plot(xvals, dat2b, 'g', alpha=0.7)
    if not nobase:
        ax2.plot(xvals, dat2c, 'm')
    lbl = 'Spectral Data, Fit, Baseline'
    if nobase:
        lbl = 'Spectral Data, Fitted Model'
    ax2.set_ylabel(lbl, fontsize=8.0)
    ax2.set_ylim(min2, max2)
    ax2.set_xlim(maxplot, minplot)
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax2.yaxis.set_major_locator(MultipleLocator(major2))        # this is for even distrib across plot
    ax2.yaxis.set_minor_locator(MultipleLocator(major2*0.5))
    # TODO bjs - from brp512 layout
    # ax0.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    # ax0.yaxis.set_minor_locator(AutoMinorLocator(2))

    
    # Noise Residual Plot -----------------------------------------------------
    
    dat1 = (freq - yfits - base)[imin:imax].real
    min1, max1 = min(dat1),max(dat1)
    delt1 = (max1 - min1)*0.75
    min1, max1 = min1 - delt1, max1 + delt1
    
    ax1 = fig.add_axes(rect1)               
    ax1.plot(xvals, dat1, 'k')
    ax1.set_ylabel('Residual', fontsize=8.0)
    ax1.set_xlabel('Chemical Shift [ppm]',         fontsize=8.0)
    ax1.set_xlim(maxplot, minplot)
    ax1.set_ylim(min2, max2)
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax1.yaxis.set_major_locator(MultipleLocator(major2))        # this is for even distrib across plot
    ax1.yaxis.set_minor_locator(MultipleLocator(major2*0.5))
    
    # Common Settings for both plot axes --------------------------------------
    
    for ax in [ax1,ax2]:
        ax.xaxis.set_major_locator(MultipleLocator(1))        # this is for even distrib across plot
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        ax.grid(which='major', axis='x', linewidth=0.50, linestyle='-', color='0.75')
        ax.grid(which='minor', axis='x', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='major', axis='y', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='minor', axis='y', linewidth=0.25, linestyle=':', color='0.75')        

    # Table Setup -------------------------------------------------------------

    ax4 = fig.add_axes(rect4)      
    ax4.xaxis.set_major_formatter(nullfmt)      # turn off axis markers
    ax4.yaxis.set_major_formatter(nullfmt)
    ax4.axis('off')

    the_table = ax4.table(cellText=fit_data, cellLoc='left',
                          colLoc='left',   colLabels=None, colWidths=None,
                          rowLoc='center', rowLabels=None,
                          fontsize=fsiz4, loc='upper center')
      
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(fsiz4)  
    for item in range(len(fit_data[0])):
        the_table.auto_set_column_width(item)   # mpl bug requires that each col be added individually
    
    table_props = the_table.properties()
    cheight = table_props['children'][0].get_height()   # all start with same default
    keys = table_props['celld'].keys()
    for key in keys:                            # use cell dict to test grid location for line settings
        cell = table_props['celld'][key]
        cell.set_height(1.0*cheight)
        cell.get_text().set_fontname(fontname)
        if key[0] in nsect:                     # this is a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'BLT'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'BRT'
            else:
                cell.visible_edges = u'BT'
            cell.set_linewidth(1.0)
            cell.set_linestyle('-')
            cell.get_text().set_fontweight('bold')
        else:                                   # not a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'L'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BL'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'R'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BR'
            else:
                cell.visible_edges = u''
                if key[0] == len(fit_data)-1:   # last line in table
                    cell.visible_edges = u'B'
            cell.set_linewidth(0.25)
            cell.set_linestyle('-')
    
    # Retrieve an element of a plot and set properties
    for tick in ax1.xaxis.get_ticklabels():
        tick.set_fontsize(8.0)
        tick.set_fontname(fontname)
        tick.set_color(local_grey)
        tick.set_weight('bold')         # 'normal'   

    for ax in [ax1,ax2]:
        ax.xaxis.label.set_fontname(fontname)
        ax.yaxis.label.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontsize(8.0)
        for tick in ax.yaxis.get_ticklabels():
            tick.set_fontsize(8.0)
            tick.set_fontname(fontname)
            tick.set_color(local_grey)
            tick.set_weight('bold')  
            tick.set_rotation(90)  

    if fixphase:
        msg = u"Vespa-Analysis Version: %s             'Fit' Tab Results  (Phase0/1 Corrected)               Processing Timestamp: %s" % (vespa_version, timestamp)
    else:
        msg = u"Vespa-Analysis Version: %s                 'Fit' Tab Results                                 Processing Timestamp: %s" % (vespa_version, timestamp)
    plt.figtext(0.042, 0.94, msg, 
                            wrap=True, 
                            horizontalalignment='left', 
                            fontsize=8, 
                            fontname=fontname)
    msg = u"VIFF File   : %s \nData Source : %s" % (viffname, data_source)
    plt.figtext(0.042, 0.89, msg, 
                            wrap=True, 
                            horizontalalignment='left',
                            color=local_grey, 
                            fontsize=10, 
                            fontname=fontname)

    
    fig.canvas.draw()
    
    return fig


def analysis_plot4(dataset, viffpath='', 
                            vespa_version='',
                            timestamp='',
                            fontname='Courier New',
                            minplot=0.1,
                            maxplot=4.9,
                            nobase=False,
                            extfig=None,
                            fixphase=False,
                            verbose=False, debug=False):
    """
    Some typical save type formats = 'svg' 'eps' 'pdf' 'png' 'raw' 'rgba' 'ps' 'pgf' etc.
    Typical fontnames  'Consolas' 'Calibri' 'Courier New' 'Times New Roman'
    
    minplot and maxplot are in PPM
    
    """
    # Print Control Setting ----------------------

    if viffpath:
        viffname = os.path.basename(viffpath)
    else:
        viffname = 'none'

    if vespa_version == '':
        vespa_version = util_misc.get_vespa_version() + ' (runtime)'
        
    if timestamp == '':
        timestamp = util_time.now().isoformat()
        
    data_source = os.path.basename(dataset.blocks["raw"].get_data_source(dataset.all_voxels[0]))
    dim0, dim1, dim2, dim3 = dataset.spectral_dims
    voxel = dataset.all_voxels

    # Process 'fit' block to get results --------------------------------------

    key = 'fit'
    if key in dataset.blocks.keys():
        block = dataset.blocks[key]
        results = block.chain.run(voxel, entry='output_refresh')

        lw    = results['fitted_lw']
        lwmin = results['minmaxlw'][0]
        lwmax = results['minmaxlw'][1]
        fit_data, nsect = dataset.blocks['fit'].results_in_table(voxel[0], lw=lw, 
                                                                           lwmin=lwmin, 
                                                                           lwmax=lwmax, 
                                                                           fixphase=fixphase,
                                                                           nozeros=False,
                                                                           noppm=False)
        nfitcol = len(fit_data[0])  
    else:
        msg = r"This dataset has no 'fit' block, returning." 
        raise ValueError(msg)

    # Gather Data -------------------------------------------------------------

    freq  = results['data'].copy() 
    base  = results['fit_baseline'].copy() 
    yfit  = results['yfit'].copy() 
    yfits = results['yfit'].copy() if len(yfit.shape)==1 else np.sum(yfit, axis=0) 
    if len(yfit.shape) == 1:
        yfit.shape = 1,yfit.shape[0]

    if fixphase:
        x,y,z = voxel[0]
        ph0  = -block.fit_results[-2,x,y,z]
        ph1  = -block.fit_results[-1,x,y,z]
        piv  = (dim0/2.0) - (dataset.frequency*(dataset.phase_1_pivot - dataset.resppm)/(dataset.sw/dim0))
        arr1 = (np.arange(dim0) - piv)/dim0
        ph0  = ph0 * DTOR
        ph1  = ph1 * DTOR * arr1
        phase  = np.exp(1j * (ph0 + ph1))
        freq  *= phase
        base  *= phase
        yfits *= phase


    # Calculate full xaxis values
    xvals = [util_ppm.pts2ppm(val, dataset) for val in range(dim0)]
    minppm, maxppm = xvals[-1], xvals[0]

    # Calculate xaxis range to plot, create tics
    minplot = minplot if minplot >= minppm else minppm
    maxplot = maxplot if maxplot <= maxppm else maxppm
    imin = int(util_ppm.ppm2pts(maxplot, dataset))
    imax = int(util_ppm.ppm2pts(minplot, dataset))
    tmin = np.round((minplot+0.5))                  # integer ppm just above minppm
    tmax = np.round((maxplot-0.5))                  # integer ppm just under maxppm
    xtick_range = np.arange(tmin, tmax+1, 1.0)
    xvals = xvals[imin:imax]                        # trim to plot width

    # Create the figure
    if extfig is None:
        fig = plt.figure(figsize=(11,8.5), facecolor='white')
    else:
        fig = extfig
        
    plt.subplots_adjust(hspace=0.001)
    nullfmt = NullFormatter()                   # used to suppress labels on an axis
    local_grey = (10./255.,10./255.,10./255.)   # used to tweak font color locally

    # Layout for an LCModel-like landscape report

    left, bottom    = 0.02, 0.07        # set up for 8.5x11 landscape printout
    w1, w2          = 0.45, 0.45
    h0, h1, h2, h3  = 0.20, 0.20, 0.20, 0.20
    hpad, vpad      = 0.04, 0.001    

    rect0 = [left+w1+hpad, bottom+h0+h1+h2, w2, h3]    # xmin, ymin, dx, and dy 
    rect1 = [left+w1+hpad, bottom+h0+h1,    w2, h2]
    rect2 = [left+w1+hpad, bottom+h0,       w2, h1]
    rect3 = [left+w1+hpad, bottom,          w2, h0]
    rect4 = [left,         bottom,          w1, h0+h1+h2+h3+0.015]

    fsiz4 = 7.0

    # Data, Fit, Baseline Plot ------------------------------------------------

    fre  = freq[imin:imax].real
    sum  = yfits[imin:imax].real
    bas  = base[imin:imax].real
    dat  = fre - bas
    fit  = sum + bas
    rsd  = fre - fit

    fre_min, fre_max = min(fre),max(fre)
    delt = (fre_max - fre_min)*0.05
    fre_min, fre_max = fre_min-delt, fre_max+delt
    tmp = abs(fre_max) if abs(fre_max) > abs(fre_min) else abs(fre_min)     # in case spectrum flipped
    fmajor = tmp/4.0
    if fmajor > 2.5: 
        fmajor = np.round(fmajor,0)

    ax0 = fig.add_axes(rect0)              
    ax0.xaxis.set_major_formatter(nullfmt)  # no x labels, have to go before plot()
    ax0.plot(xvals, fre, 'k')
    ax0.plot(xvals, fit, 'g', alpha=0.7)
    lbl = 'Data and Fit'
    ax0.set_ylabel(lbl, fontsize=8.0)
    ax0.set_ylim(fre_min, fre_max)
    ax0.set_xlim(maxplot, minplot)
    ax0.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax0.yaxis.set_major_locator(MultipleLocator(fmajor))        # this is for even distrib across plot
    ax0.yaxis.set_minor_locator(MultipleLocator(fmajor*0.5))
    # TODO bjs - from brp512 layout
    # ax0.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    # ax0.yaxis.set_minor_locator(AutoMinorLocator(2))

    # Data, baseline ----------------------------------------------------------
    
    ax1 = fig.add_axes(rect1)               
    ax1.plot(xvals, fre, 'k')
    ax1.plot(xvals, bas, 'm')
    lbl = 'Data and Base'
    ax1.set_ylabel(lbl, fontsize=8.0)
    ax1.set_ylim(fre_min, fre_max)
    ax1.set_xlim(maxplot, minplot)
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax1.yaxis.set_major_locator(MultipleLocator(fmajor))        # this is for even distrib across plot
    ax1.yaxis.set_minor_locator(MultipleLocator(fmajor*0.5))

    # Data-Base, Summed Peaks -------------------------------------------------
    
    ax2 = fig.add_axes(rect2)               
    ax2.plot(xvals, dat, 'k')
    ax2.plot(xvals, sum, 'g')
    lbl = 'Data-Base and Sum Fit'
    ax2.set_ylabel(lbl, fontsize=8.0)
    ax2.set_ylim(fre_min, fre_max)
    ax2.set_xlim(maxplot, minplot)
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax2.yaxis.set_major_locator(MultipleLocator(fmajor))        # this is for even distrib across plot
    ax2.yaxis.set_minor_locator(MultipleLocator(fmajor*0.5))
        
    # Noise Residual Plot -----------------------------------------------------
    
    ax3 = fig.add_axes(rect3)               
    ax3.plot(xvals, rsd, 'k')
    lbl = 'Residual'
    ax3.set_ylabel(lbl, fontsize=8.0)
    ax3.set_xlabel('Chemical Shift [ppm]', fontsize=8.0)
    ax3.set_ylim(fre_min, fre_max)
    ax3.set_xlim(maxplot, minplot)
    ax3.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax3.yaxis.set_major_locator(MultipleLocator(fmajor))        # this is for even distrib across plot
    ax3.yaxis.set_minor_locator(MultipleLocator(fmajor*0.5))

    # Common Settings for both plot axes --------------------------------------
    
    for ax in [ax0,ax1,ax2,ax3]:
        ax.xaxis.set_major_locator(MultipleLocator(1))        # this is for even distrib across plot
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        ax.grid(which='major', axis='x', linewidth=0.50, linestyle='-', color='0.75')
        ax.grid(which='minor', axis='x', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='major', axis='y', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='minor', axis='y', linewidth=0.25, linestyle=':', color='0.75')        

    # Table Setup -------------------------------------------------------------

    ax4 = fig.add_axes(rect4)      
    ax4.xaxis.set_major_formatter(nullfmt)      # turn off axis markers
    ax4.yaxis.set_major_formatter(nullfmt)
    ax4.axis('off')

    the_table = ax4.table(cellText=fit_data, cellLoc='left',
                          colLoc='left',   colLabels=None, colWidths=None,
                          rowLoc='center', rowLabels=None,
                          fontsize=fsiz4, loc='upper center')
      
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(fsiz4)  
    for item in range(len(fit_data[0])):
        the_table.auto_set_column_width(item)   # mpl bug requires that each col be added individually
    
    table_props = the_table.properties()
    cheight = table_props['children'][0].get_height()   # all start with same default
    keys = table_props['celld'].keys()
    for key in keys:                            # use cell dict to test grid location for line settings
        cell = table_props['celld'][key]
        cell.set_height(1.0*cheight)
        cell.get_text().set_fontname(fontname)
        if key[0] in nsect:                     # this is a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'BLT'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'BRT'
            else:
                cell.visible_edges = u'BT'
            cell.set_linewidth(1.0)
            cell.set_linestyle('-')
            cell.get_text().set_fontweight('bold')
        else:                                   # not a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'L'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BL'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'R'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BR'
            else:
                cell.visible_edges = u''
                if key[0] == len(fit_data)-1:   # last line in table
                    cell.visible_edges = u'B'
            cell.set_linewidth(0.25)
            cell.set_linestyle('-')
    
    # Retrieve an element of a plot and set properties
    for tick in ax3.xaxis.get_ticklabels():
        tick.set_fontsize(8.0)
        tick.set_fontname(fontname)
        tick.set_color(local_grey)
        tick.set_weight('bold')         # 'normal'   

    for ax in [ax0,ax1,ax2,ax3]:
        ax.xaxis.label.set_fontname(fontname)
        ax.yaxis.label.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontsize(8.0)
        for tick in ax.yaxis.get_ticklabels():
            tick.set_fontsize(8.0)
            tick.set_fontname(fontname)
            tick.set_color(local_grey)
            tick.set_weight('bold')  
            tick.set_rotation(90)  

    if fixphase:
        msg = u"Vespa-Analysis Version: %s             'Fit' Tab Results  (Phase0/1 Corrected)               Processing Timestamp: %s" % (vespa_version, timestamp)
    else:
        msg = u"Vespa-Analysis Version: %s                 'Fit' Tab Results                                 Processing Timestamp: %s" % (vespa_version, timestamp)
    plt.figtext(0.042, 0.94, msg, 
                            wrap=True, 
                            horizontalalignment='left', 
                            fontsize=8, 
                            fontname=fontname)
    msg = u"VIFF File   : %s \nData Source : %s" % (viffname, data_source)
    plt.figtext(0.042, 0.89, msg, 
                            wrap=True, 
                            horizontalalignment='left',
                            color=local_grey, 
                            fontsize=10, 
                            fontname=fontname)

    
    fig.canvas.draw()
    
    return fig


def analysis_brp512(dataset, viffpath='', 
                             vespa_version='',
                             timestamp='',
                             fontname='Courier New',
                             minplot=0.1,
                             maxplot=4.9,
                             nobase=False,
                             extfig=None,
                             fixphase=False,
                             verbose=False, 
                             debug=False):
    """
    Some typical save type formats = 'svg' 'eps' 'pdf' 'png' 'raw' 'rgba' 'ps' 'pgf' etc.
    Typical fontnames  'Consolas' 'Calibri' 'Courier New' 'Times New Roman'
    
    minplot and maxplot are in PPM
    
    """
    # Print Control Setting ----------------------

    if viffpath:
        viffname = os.path.basename(viffpath)
    else:
        viffname = 'none'

    if vespa_version == '':
        vespa_version = util_misc.get_vespa_version() + ' (runtime)'
        
    if timestamp == '':
        timestamp = util_time.now().isoformat()
        
    data_source = os.path.basename(dataset.blocks["raw"].get_data_source(dataset.all_voxels[0]))
    dim0, dim1, dim2, dim3 = dataset.spectral_dims
    voxel = dataset.all_voxels

    # Process 'fit' block to get results --------------------------------------

    key = 'fit'
    if key in dataset.blocks.keys():
        block = dataset.blocks[key]
        results = block.chain.run(voxel, entry='output_refresh')

        lw    = results['fitted_lw']
        lwmin = results['minmaxlw'][0]
        lwmax = results['minmaxlw'][1]
        fit_data, nsect = dataset.blocks['fit'].results_in_table(voxel[0], lw=lw, 
                                                                           lwmin=lwmin, 
                                                                           lwmax=lwmax, 
                                                                           fixphase=fixphase,
                                                                           nozeros=False,
                                                                           noppm=False,
                                                                           no_conf=True,
                                                                           short_form=True,
                                                                           places=4, pad=0)
        nfitcol = len(fit_data[0])  
    else:
        msg = r"This dataset has no 'fit' block, returning." 
        raise ValueError(msg)

    # Gather Data -------------------------------------------------------------

    freq  = results['data'].copy() 
    base  = results['fit_baseline'].copy() 
    yfit  = results['yfit'].copy() 
    yfits = results['yfit'].copy() if len(yfit.shape)==1 else np.sum(yfit, axis=0) 
    if len(yfit.shape) == 1:
        yfit.shape = 1,yfit.shape[0]

    if fixphase:
        x,y,z = voxel[0]
        ph0  = -block.fit_results[-2,x,y,z]
        ph1  = -block.fit_results[-1,x,y,z]
        piv  = (dim0/2.0) - (dataset.frequency*(dataset.phase_1_pivot - dataset.resppm)/(dataset.sw/dim0))
        arr1 = (np.arange(dim0) - piv)/dim0
        ph0  = ph0 * DTOR
        ph1  = ph1 * DTOR * arr1
        phase  = np.exp(1j * (ph0 + ph1))
        freq  *= phase
        base  *= phase
        yfits *= phase


    # Calculate full xaxis values
    xvals = [util_ppm.pts2ppm(val, dataset) for val in range(dim0)]
    minppm, maxppm = xvals[-1], xvals[0]

    # Calculate xaxis range to plot, create tics 
    minplot = minplot if minplot >= minppm else minppm
    maxplot = maxplot if maxplot <= maxppm else maxppm
    imin = int(util_ppm.ppm2pts(maxplot, dataset))
    imax = int(util_ppm.ppm2pts(minplot, dataset))
    tmin = np.round((minplot+0.5))                  # integer ppm just above minppm
    tmax = np.round((maxplot-0.5))                  # integer ppm just under maxppm
    xtick_range = np.arange(tmin, tmax+1, 1.0)
    xvals = xvals[imin:imax]                        # trim to plot width

    # Create the figure
    if extfig is None: 
        fig = plt.figure(figsize=(8,8), dpi=64, facecolor='white')
    else:
        fig = extfig 
        
    plt.subplots_adjust(hspace=0.001)
    nullfmt = NullFormatter()                   # used to suppress labels on an axis
    #local_grey = (10./255.,10./255.,10./255.)   # used to tweak font color locally
    local_grey = 'black'   # used to tweak font color locally

    # Layout for an LCModel-like landscape report

    left, bottom    = 0.005, 0.05        # set up for 8.5x11 landscape printout
    w1, w2          = 0.51,  0.43
    h0, h1, h2, h3  = 0.215,  0.215, 0.215, 0.215
    hpad, vpad      = 0.04,  0.001    

    rect0 = [left+w1+hpad, bottom+h0+h1+h2, w2, h3]    # xmin, ymin, dx, and dy 
    rect1 = [left+w1+hpad, bottom+h0+h1,    w2, h2]
    rect2 = [left+w1+hpad, bottom+h0,       w2, h1]
    rect3 = [left+w1+hpad, bottom,          w2, h0]
    rect4 = [left,         bottom,          w1, h0+h1+h2+h3+0.015]

    fsiz4 = 9.0

    # Data, Fit, Baseline Plot ------------------------------------------------

    fre  = freq[imin:imax].real
    sum  = yfits[imin:imax].real
    bas  = base[imin:imax].real
    dat  = fre - bas
    fit  = sum + bas
    rsd  = fre - fit

    fre_min, fre_max = min(fre),max(fre)
    delt = (fre_max - fre_min)*0.05
    fre_min, fre_max = fre_min-delt, fre_max+delt
#    tmp = abs(fre_max) if abs(fre_max) > abs(fre_min) else abs(fre_min)     # in case spectrum flipped
#    fmajor = tmp/4.0
#    if fmajor > 2.5: 
#        fmajor = np.round(fmajor,0)

    ax0 = fig.add_axes(rect0)              
    ax0.xaxis.set_major_formatter(nullfmt)  # no x labels, have to go before plot()
    ax0.plot(xvals, fre, 'k')
    ax0.plot(xvals, fit, 'g', alpha=0.7)
    lbl = 'Data and Fit'
    ax0.set_ylabel(lbl, fontsize=fsiz4)
    ax0.set_ylim(fre_min, fre_max)
    ax0.set_xlim(maxplot, minplot)
    ax0.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax0.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    ax0.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax0.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    # Data, baseline ----------------------------------------------------------
    
    ax1 = fig.add_axes(rect1)               
    ax1.plot(xvals, fre, 'k')
    ax1.plot(xvals, bas, 'm')
    lbl = 'Data and Base'
    ax1.set_ylabel(lbl, fontsize=fsiz4)
    ax1.set_ylim(fre_min, fre_max)
    ax1.set_xlim(maxplot, minplot)
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    # Data-Base, Summed Peaks -------------------------------------------------
    
    ax2 = fig.add_axes(rect2)               
    ax2.plot(xvals, dat, 'k')
    ax2.plot(xvals, sum, 'g')
    lbl = 'Data-Base and Sum Fit'
    ax2.set_ylabel(lbl, fontsize=fsiz4)
    ax2.set_ylim(fre_min, fre_max)
    ax2.set_xlim(maxplot, minplot)
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax2.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        
    # Noise Residual Plot -----------------------------------------------------
    
    ax3 = fig.add_axes(rect3)               
    ax3.plot(xvals, rsd, 'k')
    lbl = 'Residual'
    ax3.set_ylabel(lbl, fontsize=fsiz4)
    ax3.set_xlabel('Chemical Shift [ppm]', fontsize=fsiz4)
    ax3.set_ylim(fre_min, fre_max)
    ax3.set_xlim(maxplot, minplot)
    ax3.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax3.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper', integer=True, min_n_ticks=3))
    ax3.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    # Common Settings for both plot axes --------------------------------------
    
    for ax in [ax0,ax1,ax2,ax3]:
        ax.xaxis.set_major_locator(MultipleLocator(1))        # this is for even distrib across plot
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        ax.grid(which='major', axis='x', linewidth=0.50, linestyle='-', color='0.75')
        ax.grid(which='minor', axis='x', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='major', axis='y', linewidth=0.25, linestyle=':', color='0.75')
        ax.grid(which='minor', axis='y', linewidth=0.25, linestyle=':', color='0.75')       

    # Table Setup -------------------------------------------------------------

    ax4 = fig.add_axes(rect4)      
    ax4.xaxis.set_major_formatter(nullfmt)      # turn off axis markers
    ax4.yaxis.set_major_formatter(nullfmt)
    ax4.axis('off')

    the_table = ax4.table(cellText=fit_data, cellLoc='left',
                          colLoc='left',   colLabels=None, colWidths=None,
                          rowLoc='center', rowLabels=None,
                          fontsize=fsiz4, loc='upper center')
      
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(fsiz4)  
    for item in range(len(fit_data[0])):
        the_table.auto_set_column_width(item)   # mpl bug requires that each col be added individually
    
    table_props = the_table.properties()
    cheight = table_props['children'][0].get_height()   # all start with same default
    keys = table_props['celld'].keys()
    for key in keys:                            # use cell dict to test grid location for line settings
        cell = table_props['celld'][key]
        cell.set_height(1.0*cheight)
        cell.get_text().set_fontname(fontname)
        if key[0] in nsect:                     # this is a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'BLT'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'BRT'
            else:
                cell.visible_edges = u'BT'
            cell.set_linewidth(1.0)
            cell.set_linestyle('-')
            #cell.get_text().set_fontweight('bold')
        else:                                   # not a header cell
            if key[1] == 0:                     # - leftmost
                cell.visible_edges = u'L'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BL'
            elif key[1] == nfitcol-1:           # - rightmost
                cell.visible_edges = u'R'
                if key[0] == len(fit_data)-1:
                    cell.visible_edges = u'BR'
            else:
                cell.visible_edges = u''
                if key[0] == len(fit_data)-1:   # last line in table
                    cell.visible_edges = u'B'
            cell.set_linewidth(0.75)
            cell.set_linestyle('-')
            #cell.get_text().set_fontweight('bold')
    
    # Retrieve an element of a plot and set properties
    for tick in ax3.xaxis.get_ticklabels():
        tick.set_fontsize(fsiz4)
        tick.set_fontname(fontname)
        tick.set_color(local_grey)
        #tick.set_weight('bold')         # 'normal'   

    for ax in [ax0,ax1,ax2,ax3]:
        ax.xaxis.label.set_fontname(fontname) 
        ax.yaxis.label.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontname(fontname)
        ax.yaxis.offsetText.set_fontsize(fsiz4)
        for tick in ax.yaxis.get_ticklabels():
            tick.set_fontsize(fsiz4)
            tick.set_fontname(fontname)
            tick.set_color(local_grey)
            #tick.set_weight('bold')  
            tick.set_rotation(90)  

    if fixphase:
        msg = u"Vespa-Analysis v%s   ICE Inline Processing (Phase0/1 Corr)    Timestamp: %s" % (vespa_version, timestamp)
        #msg = u"Vespa-Analysis v%s   ICE Inline Processing (Phase0/1 Corr)    Timestamp: %s" % ('0.9.x', '2017-11-07T11:30:35')
    else:
        msg = u"Vespa-Analysis v%s                Inline Processing                 Timestamp: %s" % (vespa_version, timestamp)
    
    fig.text(0.042, 0.93, msg, 
                    wrap=True, 
                    horizontalalignment='left', 
                    fontsize=fsiz4, 
                    fontname=fontname)

    
    fig.canvas.draw()

#    buf = fig.canvas.tostring_rgb()
#
#     ncols, nrows = fig.canvas.get_width_height()
#     
#     cbuf = np.fromstring(buf, dtype=np.uint8)
#     cbuf = tuple([int(item) for item in cbuf])
#     
#     bob = np.fromstring(buf, dtype=np.uint8).reshape(int(nrows*ncols*3/16),16)
# 
#     fname1 = "D:\\Users\\bsoher\\_test1.txt"
#     fname2 = "D:\\Users\\bsoher\\_test1.bin"
#     hdr    = 'const char myarr[] = {'
#     ftr    = '};'
#     
#     np.savetxt(fname1, bob, fmt='%d', delimiter=',', newline='\n', header=hdr, footer=ftr)
#     bob.tofile(fname2)

     
    return fig 


# Testing utilities -----------------------------------------------------------

def _open_viff(datafile):
    
    datasets = []

    filename = datafile
    timestamp = ''

    msg = ""
    try:
        importer = util_import.DatasetCliImporter(filename)
    except IOError:
        msg = """I can't read the file "%s".""" % filename
    except SyntaxError:
        msg = """The file "%s" isn't valid Vespa Interchange File Format.""" % filename


    if msg:        
        print >> sys.stderr, msg
        print >> sys.stdout, msg
        sys.exit(-1)
    else:
        # Time to rock and roll!
        dsets, timestamp = importer.go()

        for item in dsets:
            datasets.append(item)


    if datasets:

        for dataset in datasets:
            if dataset.id == datasets[-1].id:
                dataset.dataset_filename = filename
                # dataset.filename is an attribute set only at run-time
                # to maintain the name of the VIFF file that was read in
                # rather than deriving a filename from the raw data
                # filenames with *.xml appended. But we need to set this
                # filename only for the primary dataset, not the associated
                # datasets. Associated datasets will default back to their
                # raw filenames if we go to save them for any reason
            else:
                dataset.dataset_filename = ''

    return datasets, timestamp



def main():
    """ Now we have a test """
    
    STARTDIR = 'D:\\Users\\bsoher\\code\\repository_svn\\sample_data\\figure_layout_viffs' 
    viffpath = STARTDIR+'\\oneil_5076.0002.xml'

    savetype    = 'pdf'
#    savetype    = 'png'
    minplot     = 0.1
    maxplot     = 4.9
    fixphase    = True
    fontname    = 'Courier New'

    vespa_version = util_misc.get_vespa_version()

    # Check a few things up front ----------------
        
    if not os.path.isfile(viffpath):
        msg = """VIFF FILE does not exist "%s".""" % viffpath 
        print >> sys.stderr, msg
        print >> sys.stdout, msg
        sys.exit(-1)

    fsupported = plt.gcf().canvas.get_supported_filetypes()
    if savetype not in fsupported.keys():
        msg = r"Output file format '%s' not supported by current Matplotlib backend, Returning." % savetype
        raise ValueError(msg)
            
    # Load Main Dataset --------------------------
    
    datasets, timestamp = _open_viff(viffpath)
        
    dataset = datasets[-1]
    outbase = viffpath+'.metab'
    
    # Print Control Setting ----------------------

    fig = figure_layouts.analysis_plot2(dataset, 
                                  viffpath=viffpath, 
                                  vespa_version=vespa_version,
                                  timestamp=timestamp,
                                  fontname=fontname,
                                  minplot=minplot,
                                  maxplot=maxplot,
                                  nobase=True,
                                  extfig=None,
                                  fixphase=fixphase,
                                  verbose=False, debug=False)
 
    outname = outbase+'.'+savetype
 
    fig.savefig(outname, dpi=300, pad_inches=0.5)
    
    print "Testing completed successfully ... returning."
            
            
if __name__ == '__main__':
    main()        











#     # no labels
#     nullfmt = NullFormatter()         # no labels
#
#     ax4.xaxis.set_major_formatter(nullfmt)  # have to go before plot()
#     ax4.yaxis.set_major_formatter(nullfmt)  # have to go before plot()
#     ax4.plot(freq[1000:1800])
#     plt.xticks(np.arange(100, 800, 200))
#     plt.xlim(0, 800)


#     # Gets rid of xaxis label for ax1 and ax2
#     xticklabels = ax1.get_xticklabels() + ax2.get_xticklabels()
#     plt.setp(xticklabels, visible=False)
   

#     # Annotate example with mathtext and how to set color with 3 term RGB vector
#     mpl_grey_rvb = (51./255., 51./255., 51./255.)
#     mpl_grey_rvb = (1./255., 1./255., 1./255.)
#     tmp2 =r"$\mathrm{Roman}\ , \ \mathit{Italic}\ , \ \mathtt{Typewriter} \, \ \mathrm{or}\ \mathcal{CALLIGRAPHY}$"
#     plt.annotate(tmp2,  xy=(110.0, 7.0),
#                         xycoords='data', 
#                         color=mpl_grey_rvb,
#                         fontsize=7)        