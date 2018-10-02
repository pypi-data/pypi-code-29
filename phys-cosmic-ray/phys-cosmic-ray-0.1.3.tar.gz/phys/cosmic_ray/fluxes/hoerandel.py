from phys import units
import numpy

def hoerandel_flux(energy, ptype):
    """
    All-particle spectrum (up to iron) after Hoerandel_

    .. _Hoerandel: http://dx.doi.org/10.1016/S0927-6505(02)00198-6
    """
    delta_gamma = 2.1
    eps_cutoff = 1.9
    E_knee = 4.49*units.PeV
    if ptype < 100:
        Z = 1
    else:
        Z = ptype % 100

    ptypes = numpy.array([
        14,   402,  703,  904,  1105, 1206, 1407, 1608, 1909, 2010,
        2311, 2412, 2713, 2814, 3115, 3216, 3517, 4018, 3919, 4020,
        4521, 4822, 5123, 5224, 5525, 5626
    ])
    idx = numpy.where(ptypes == ptype)
    if not idx:
        raise Exception('Unknown particle type %s. The known types are:\n  %s'%(ptype, ', '.join(ptypes)))
    gamma = numpy.array([
        2.71, 2.64, 2.54, 2.75, 2.95, 2.66, 2.72, 2.68, 2.69, 2.64,
        2.66, 2.64, 2.66, 2.75, 2.69, 2.55, 2.68, 2.64, 2.65, 2.7,
        2.64, 2.61, 2.63, 2.67, 2.46, 2.59
    ])
    flux = numpy.array([
        0.0873,   0.0571,  0.00208, 0.000474, 0.000895, 0.0106,  0.00235,  0.0157,   0.000328, 0.0046,
        0.000754, 0.00801, 0.00115, 0.00796,  0.00027,  0.00229, 0.000294, 0.000836, 0.000536, 0.00147,
        0.000304, 0.00113, 0.000631, 0.00136, 0.00135,  0.0204
    ])/(units.m2*units.sr*units.s*units.TeV)

    return flux[idx]*(energy/units.TeV)**(-gamma[idx])*(1+(energy/(E_knee*Z))**eps_cutoff)**(-delta_gamma/eps_cutoff)
