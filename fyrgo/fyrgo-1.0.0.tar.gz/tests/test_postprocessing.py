import pathlib
import numpy as np
import fyrgo as fy

fyloc = fy.__path__[0]
fypath = pathlib.Path(fyloc)
datapath = str(fypath.parent / 'data')

def eval_err(a,b) :
    err = np.mean(np.abs((b-a)))
    return err

def remove_hill_rings(a):
    return np.array(list(a[:112])+list(a[125:]))

def test_torque():
    dl = fy.DataLoader(
        configfile = datapath + '/config.par',
        outputdir  = datapath,
        offsets    = [50,55]
    )
    off = 50
    told = dl["torque1D0"][off]
    xp = dl['planet'][0].x[off]
    yp = dl['planet'][0].y[off]
    tnew = fy.torque_from_density(dl, off, xp, yp)
    tnew_cut = remove_hill_rings(tnew)
    told_cut = remove_hill_rings(told)
    err = eval_err(told_cut, tnew_cut)
    assert(err < 5e-8)
    return told, tnew


if __name__=='__main__':
    import matplotlib.pyplot as plt
    to, tn = test_torque()
    fig,ax = plt.subplots()
    ax.plot(remove_hill_rings(to))
    ax.plot(remove_hill_rings(tn))
    ax.plot(to)
    ax.plot(tn)
    plt.ion()
    plt.show()
    fig.savefig('torques_methods.png')
