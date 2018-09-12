# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:28:39 2018

@author: tb267
"""

import pyaudio
import numpy as np
import pyqtgraph as pg






class mySettings(object):
    '''
    A class that stores the acquisition settings.
    
    Attributes:
    --------------       
    channels: int
        Number of Channels
    fs: int
        Sampling Frequency
    nbits: int
        Number of bits - either 8, 16, 24 or 32
    chunk_size: int
        Number of samples obtained from each channel in one chunk
    num_chunks: int
        Number of chunks to store in circular buffer
    view_time: float
        If specified, overrides num_chunks to display view_time in seconds for oscilloscope
    stored_time: float
        Length of the pre-trigger when the space button is hit, in seconds
    device_index: int
        device index, will prompt if not specified
    init_view_time: bool
        flag for time domain view in oscilloscope
    init_view_freq: bool
        flag for frequency domain view in oscilloscope
    init_view_levels: bool
        flag for channel levels view in oscilloscope
    '''
        
    def __init__(self, *, 
                 channels=2, 
                 fs=44100, 
                 nbits=16, 
                 chunk_size=1024, 
                 num_chunks=6,
                 view_time=None,
                 stored_time=2,
                 device_index=None,
                 init_view_time=True,
                 init_view_freq=True,
                 init_view_levels=True):
        
        self.channels=channels
        self.fs=fs
        self.chunk_size=chunk_size
        self.num_chunks=num_chunks
        self.view_time=view_time
        self.nbits=nbits
        self.stored_time=stored_time
        self.device_index=device_index
        self.init_view_time=init_view_time
        self.init_view_freq=init_view_freq
        self.init_view_levels=init_view_levels
        
        ### derived settings
        if view_time != None:
            self.num_chunks = int(np.ceil(view_time*fs/chunk_size))
            
        self.format = eval('pyaudio.paInt'+str(self.nbits))
        self.device_name = None # until initialise stream
        
    
    def __repr__(self):
        return '<mySettings class>'
        
    
        
        
def set_plot_colours(channels):
    '''
    Returns a list of RGB colours depending on the number of channels required.
    '''
    #TODO: Accessible colours
    val = [0.0,0.5,1.0]
    colour = np.array([[255,0,0,255],[0,255,0,255],[0,0,255,255]], dtype = np.ubyte)
    plot_colourmap =  pg.ColorMap(val,colour)
    c_list = plot_colourmap.getLookupTable(nPts =channels,alpha=True)
    return c_list 
