import pathlib

import fyrgo as fy

fyloc = fy.__path__[0]
fypath = pathlib.Path(fyloc)
datapath = fypath.parent / 'data'

def test_load_from_pathlib():
    args = dict(configfile = datapath / 'config.par',
                outputdir  = datapath)
    dl = fy.DataLoader(**args)
    assert(dl.configfile == str(datapath / 'config.par'))
    assert(dl.outputdir == str(datapath))

def test_load_exception():
    #todo : use pytest marker for 'expected to fail' test
    try:
        fy.DataLoader(
            configfile=datapath / 'config.par',
            outputdir='some_imaginary_path'
        )
    except AssertionError:
        pass
    assert(1)

def test_guess_outputdir():
    dl = fy.DataLoader(configfile = datapath / 'config.par')
    assert(dl.outputdir == str(datapath))
