import numpy as np
from mountainlab_pytools import mdaio

class TimeseriesMdaReader:
    def __init__(self,path,*,samplerate):
        self._samplerate=samplerate
        self._mda_path=path
        X=mdaio.DiskReadMda(path)
        self._num_channels=X.N1()
        self._num_timepoints=X.N2()
    def numChannels(self):
        return self._num_channels
    def numTimepoints(self):
        return self._num_timepoints
    def sampleRate(self):
        return self._samplerate
    def getChunk(self,*,trange=None,channels=None):
        if not channels:
            channels=range(1,self._num_channels+1)
        if not trange:
            trange=[0,self._num_timepoints]
        X=mdaio.DiskReadMda(self._mda_path)
        chunk=X.readChunk(i1=0,i2=trange[0],N1=self._num_channels,N2=trange[1]-trange[0])
        return chunk[np.array(channels)-1,:]
