from phys import units
import numpy

class ParticleType(object):
    PPlus       =   14
    He4Nucleus  =  402
    N14Nucleus  = 1407
    Al27Nucleus = 2713
    Fe56Nucleus = 5626
    Te72Nucleus = 7252
    Hg120Nucleus = 12080

_codes_ = sorted(filter(lambda v: isinstance(v, int), ParticleType.__dict__.values()))

def gst_flux(energy, ptype=14, populations=None):
    """
    Evaluate the GST parameterization of the cosmic ray flux.

    Parameters
    ----------
    energy: array-like
    ptype: integer
        The particle code representing the mass group. Allowed particle codes are:
          - proton:           14
          - Helium:           402
          - Nitrogen   (CNO): 1407
          - Aluminum (Mg-Si): 2713
          - Iron:             5626
          - Tellurium:        7252
          - Mercury:          12080
    """
    if ptype < 100:
        z = 1
    else:
        z = ptype % 100
    idx = _codes_.index(ptype)
    norm = numpy.array([
        [7000, 3200, 100,   130,   60,    0,   0],
        [150,  65,   6,     7,     2.3,   0.1, 0.4],
        #[150,  65,   6,     7,     2.3,   0., 0.],
        [14,   0.07, 0.006, 0.007, 0.025, 0,   0]
        #[14,   0., 0., 0., 0.025, 0,   0]
    ])/(units.m2*units.sr*units.s*units.GeV)
    if not populations is None:
        for i in range(len(norm)):
            if i in populations: continue
            norm[i] = [0]*len(norm[i])
    gamma = numpy.array([
        [2.66, 2.58, 2.4, 2.4, 2.3, 0,   0],
        [2.4,  2.3,  2.3, 2.3, 2.2, 2.2, 2.2],
        [2.4,  2.3,  2.3, 2.3, 2.2, 0,   0]
    ])
    rigidity = numpy.array([
        120e3, 4e6, 1.3e9
    ])*units.GeV
    return sum(n[idx]*(energy/units.GeV)**(-g[idx])*numpy.exp(-energy/(r*z)) for n, g, r in zip(norm, gamma, rigidity))

def gst_flux2(energy, ptype=14, populations=None):
    """
    Evaluate the GST parameterization of the cosmic ray flux.

    Parameters
    ----------
    energy: array-like
    ptype: integer
        The particle code representing the mass group. Allowed particle codes are:
          - proton:           14
          - Helium:           402
          - Nitrogen   (CNO): 1407
          - Aluminum (Mg-Si): 2713
          - Iron:             5626
          - Tellurium:        7252
          - Mercury:          12080
    """
    if ptype < 100:
        z = 1
    else:
        z = ptype % 100
    idx = _codes_.index(ptype)
    norm = numpy.array([
        [7000, 3200, 100,   130,   60,    0,   0],
        #[150,  65,   6,     7,     2.3,   0.1, 0.4],
        [150,  65,   6,     7,     2.3,   0., 0.],
        #[14,   0.07, 0.006, 0.007, 0.025, 0,   0]
        [14,   0., 0., 0., 0.025, 0,   0]
    ])/(units.m2*units.sr*units.s*units.GeV)
    if not populations is None:
        for i in range(len(norm)):
            if i in populations: continue
            norm[i] = [0]*5
    gamma = numpy.array([
        [2.66, 2.58, 2.4, 2.4, 2.3, 0,   0],
        [2.4,  2.3,  2.3, 2.3, 2.2, 2.2, 2.2],
        [2.4,  2.3,  2.3, 2.3, 2.2, 0,   0]
    ])
    rigidity = numpy.array([
        120e3, 4e6, 1.3e9
    ])*units.GeV
    return sum(n[idx]*(energy/units.GeV)**(-g[idx])*numpy.exp(-energy/(r*z)) for n, g, r in zip(norm, gamma, rigidity))
