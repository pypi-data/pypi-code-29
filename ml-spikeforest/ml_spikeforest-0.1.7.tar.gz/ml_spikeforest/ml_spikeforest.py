#!/usr/bin/env python3

import sys

from mlprocessors.registry import registry, register_processor

registry.namespace = "spikeforest"

from mlprocessors.core import Input, Output, Processor, IntegerParameter, FloatParameter, StringParameter, IntegerListParameter

import os
from shutil import copyfile
import subprocess, shlex
import h5py
from mountainlab_pytools import mdaio
import numpy as np
    
def prepare_timeseries_hdf5(timeseries_fname,timeseries_hdf5_fname,*,chunk_size,padding,samplerate):
    chunk_size_with_padding=chunk_size+2*padding
    with h5py.File(timeseries_hdf5_fname,"w") as f:
        X=mdaio.DiskReadMda(timeseries_fname)
        M=X.N1() # Number of channels
        N=X.N2() # Number of timepoints
        num_chunks=int(np.ceil(N/chunk_size))
        f.attrs['chunk_size']=chunk_size
        f.attrs['num_chunks']=num_chunks
        f.attrs['padding']=padding
        f.attrs['num_channels']=M
        f.attrs['num_timepoints']=N
        f.attrs['samplerate']=samplerate
        for j in range(num_chunks):
            padded_chunk=np.zeros((X.N1(),chunk_size_with_padding),dtype=X.dt())    
            t1=int(j*chunk_size) # first timepoint of the chunk
            t2=int(np.minimum(X.N2(),(t1+chunk_size))) # last timepoint of chunk (+1)
            s1=int(np.maximum(0,t1-padding)) # first timepoint including the padding
            s2=int(np.minimum(X.N2(),t2+padding)) # last timepoint (+1) including the padding
            
            # determine aa so that t1-s1+aa = padding
            # so, aa = padding-(t1-s1)
            aa = padding-(t1-s1)
            padded_chunk[:,aa:aa+s2-s1]=X.readChunk(i1=0,N1=X.N1(),i2=s1,N2=s2-s1) # Read the padded chunk

            for m in range(1,M+1):
                f.create_dataset('parts/channel-{}/chunk-{}'.format(m,j),data=padded_chunk[m-1,:].ravel())

@register_processor(registry)
class create_timeseries_hdf5(Processor):
    """
        Create a .hdf5 file containing a chunked timeseries
    """
    VERSION='0.1.3'

    input = Input('Input timeseries .mda file (MxN) M=number of channels, N=number of timepoints')
    output = Output('Output timeseries .hdf5 file with chunks of data.')

    samplerate = FloatParameter(description="Sampling rate (Hz)")
    chunk_size = IntegerParameter(description="Time chunk size for data in hdf5 file.",optional=True,default=1e6)
    chunk_padding = IntegerParameter(description="Time chunk padding size for data in hdf5 file.",optional=True,default=1e3)


    def run(self):
        #tmpdir=os.environ.get('ML_PROCESSOR_TEMPDIR')
        hdf5_chunk_size=int(self.chunk_size)
        hdf5_padding=int(self.chunk_padding)
        prepare_timeseries_hdf5(self.input,self.output,chunk_size=hdf5_chunk_size,padding=hdf5_padding,samplerate=self.samplerate)
        return True

if __name__ == "__main__":
    registry.process(sys.argv)
