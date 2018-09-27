import pathlib

import numpy as np

import fyrgo as fy

fyloc = fy.__path__[0]
fypath = pathlib.Path(fyloc)

def test_planet_auto_load():
    datapath = str(fypath.parent / 'data/')
    dl  = fy.DataLoader(datapath+'/config.par', datapath, offsets=100)
    raw = np.loadtxt(datapath + '/acc0.dat')
    assert(len(dl.planets['acc'][0].columns)==raw.shape[1])
