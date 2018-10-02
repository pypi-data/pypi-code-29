from phys import units
import numpy

class ParticleType(object):
    PPlus       =   14
    He4Nucleus  =  402
    N14Nucleus  = 1407
    Al27Nucleus = 2713
    Fe56Nucleus = 5626

_codes_ = sorted(filter(lambda v: isinstance(v, int), ParticleType.__dict__.values()))

def atomic_mass(code):
    return numpy.floor(code/100)

def gaisser_h3a_flux(energy, ptype=14, populations=None):
    """
    Evaluate the [Gaisser]_ H3a parameterization of the cosmic ray flux.

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
    """
    if ptype < 100:
        z = 1
    else:
        z = ptype % 100
    idx = _codes_.index(ptype)
    norm = numpy.array([
        [7860., 3550., 2200., 1430., 2120.],
        [20]*2 + [13.4]*3,
        [1.7]*2 + [1.14]*3
    ])/(units.m2*units.sr*units.s*units.GeV)
    if not populations is None:
        for i in range(len(norm)):
            if i in populations: continue
            norm[i] = [0]*5
    gamma = [
        [2.66, 2.58, 2.63, 2.67, 2.63],
        [2.4]*5,
        [2.4]*5
    ]
    rigidity = numpy.array([
        4e6, 30e6, 2e9
    ])*units.GeV
    return sum(n[idx]*(energy/units.GeV)**(-g[idx])*numpy.exp(-energy/(r*z)) for n, g, r in zip(norm, gamma, rigidity))

def gaisser_h4a_flux(energy, ptype=14, populations=None):
    """
    Evaluate the [Gaisser]_ H3a parameterization of the cosmic ray flux.

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
    """
    if ptype < 100:
        z = 1
    else:
        z = ptype % 100
    idx = _codes_.index(ptype)
    norm = numpy.array([
        [7860., 3550., 2200., 1430., 2120.],
        [20]*2 + [13.4]*3,
        [200] + [0]*4
    ])/(units.m2*units.sr*units.s*units.GeV)
    if not populations is None:
        for i in range(len(norm)):
            if i in populations: continue
            norm[i] = [0]*5
    gamma = [
        [2.66, 2.58, 2.63, 2.67, 2.63],
        [2.4]*5,
        [2.6] + [0]*4
    ]
    rigidity = numpy.array([
        4e6, 30e6, 6e10
    ])*units.GeV
    return sum(n[idx]*(energy/units.GeV)**(-g[idx])*numpy.exp(-energy/(r*z)) for n, g, r in zip(norm, gamma, rigidity))

def gaisser_flux_new(E):
    gamma, delta, Estar, eps = 2.65, 0.75, 1.2E+06*units.GeV,3.
    return (1.15*E**(-gamma)*(1+(E/Estar)**eps)**(-delta/eps))*10**4
