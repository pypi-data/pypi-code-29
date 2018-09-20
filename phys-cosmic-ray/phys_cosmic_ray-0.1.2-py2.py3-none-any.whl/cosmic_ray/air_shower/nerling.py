"""
From F. Nerling, J. Blumer, R. Engel, and M. Risse, Astropart.
Phys. 24, 421 (2006).
"""

import numpy
import scipy.interpolate
from phys import units

# energy cut in MeV
_k_params_ = numpy.array([[ 0.05    ,  0.1     ,  0.25    ,  0.5     ,  1.      ,  2.      ],
                          [ 0.141866,  0.142049,  0.142589,  0.143458,  0.145098,  0.148071],
                          [ 6.17963 ,  6.18075 ,  6.18413 ,  6.18979 ,  6.20114 ,  6.22334 ],
                          [-0.606055, -0.605484, -0.603838, -0.601298, -0.596851, -0.58971 ]])

_k = [scipy.interpolate.interp1d(_k_params_[0], _k_params_[i]) for i in range(1,4)]

def e_spectrum_norm(E, s, e_cut=0.05*units.MeV):
    """
    The normalized electron energy spectrum (f(E,s) = \frac{1}{N} \frac{dN}{d \ln E}).

    It is normalized in the energy interval (e_cut, \infty). The energy cut can be in the range (50 keV, 2 MeV).
    """
    e_cut = e_cut/units.MeV
    E = E/units.MeV
    a1 = 6.42522 - 1.53183*s
    a2 = 168.168 - 42.1368*s
    a0 = _k[0](e_cut) * numpy.exp(_k[1](e_cut)*s + _k[2](e_cut)*s**2)
    return a0*E/((E + a1)*(E + a2)**s)
