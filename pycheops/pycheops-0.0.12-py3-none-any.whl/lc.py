# -*- coding: utf-8 -*-
#
#   pycheops - Tools for the analysis of data from the ESA CHEOPS mission
#
#   Copyright (C) 2018  Dr Pierre Maxted, Keele University
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""
lc
=======
 
 Functions for calculating light curves of transiting exoplanets.

Functions 
---------
"""

from __future__ import (absolute_import, division, print_function,
                                unicode_literals)
from numpy import arccos, sqrt, pi, clip, select, finfo, cos, ones_like
from warnings import warn
from numba import jit

__all__ = [ 'qpower2','ueclipse']

@jit(nopython=True)
def qpower2(z,p,c,a):
    """
    Fast and accurate transit light curves for the power-2 limb-darkening law

    The power-2 limb-darkening law is I(mu) = 1 - c (1 - mu**a)

    Light curves are calculated using the qpower2 approximation [1]. The
    approximation is accurate to better than 100ppm for radius ratio p < 0.1.

    N.B. qpower2 is untested/inaccurate for values of p > 0.2

    .. [1] Maxted, P.F.L.  & Gill, S. in prep, 2018

    :param z: star-planet separation on the sky cf. star radius (array)
    :param p: planet-star radius ratio (scalar, p<1) 
    :param c: power-2 limb darkening coefficient
    :param a: power-2 limb darkening exponent

    :returns: light curve (observed flux)  
    
    """

    if (p > 1):
        raise ValueError("qpower2 requires p < 1")

    if (p > 0.2):
        warn ("qpower2 is untested/inaccurate for values of p > 0.2")

    f = ones_like(z)
    I_0 = (a+2)/(pi*(a-c*a+2))
    g = 0.5*a
    for i,zi in enumerate(z):
        zt = abs(zi)
        if zt <= (1-p):
            s = 1-zt**2
            c0 = (1-c+c*s**g)
            c2 = 0.5*a*c*s**(g-2)*((a-1)*zt**2-1)
            f[i] = 1-I_0*pi*p**2*(
                    c0 + 0.25*p**2*c2 - 0.125*a*c*p**2*s**(g-1) )
        elif abs(zt-1) < p:
            d = (zt**2 - p**2 + 1)/(2*zt)
            ra = 0.5*(zt-p+d)
            rb = 0.5*(1+d)
            sa = 1-ra**2
            sb = 1-rb**2
            q = min(max(-1,(zt-d)/p),1)
            w2 = p**2-(d-zt)**2
            w = sqrt(w2)
            b0 = 1 - c + c*sa**g
            b1 = -a*c*ra*sa**(g-1)
            b2 = 0.5*a*c*sa**(g-2)*((a-1)*ra**2-1)
            a0 = b0 + b1*(zt-ra) + b2*(zt-ra)**2
            a1 = b1+2*b2*(zt-ra)
            aq = arccos(q)
            J1 = ( (a0*(d-zt)-(2/3)*a1*w2 + 
                0.25*b2*(d-zt)*(2*(d-zt)**2-p**2))*w
                 + (a0*p**2 + 0.25*b2*p**4)*aq )
            J2 = a*c*sa**(g-1)*p**4*(
                0.125*aq + (1/12)*q*(q**2-2.5)*sqrt(max(0,1-q**2)) )
            d0 = 1 - c + c*sb**g
            d1 = -a*c*rb*sb**(g-1)
            K1 = ((d0-rb*d1)*arccos(d) + 
                    ((rb*d+(2/3)*(1-d**2))*d1 - d*d0)*sqrt(max(0,1-d**2)) )
            K2 = (1/3)*c*a*sb**(g+0.5)*(1-d)
            f[i] = 1 - I_0*(J1 - J2 + K1 - K2)
    return f

@jit(nopython=True)
def ueclipse(z,p,f):
    """
    Eclipse light curve for a planet with uniform surface brightness by a star

    :param z: star-planet separation on the sky cf. star radius (array)
    :param p: planet-star radius ratio (scalar, p<1) 
    :param f: planet-star flux ratio (scalar) 

    :returns: light curve (observed flux)  
    
    """
    if (p > 1):
        raise ValueError("ueclipse requires p < 1")

    fl = ones_like(z)
    for i,zi in enumerate(z):
        zt = abs(zi)
        if zt <= (1-p):
            fl[i] = 1/(1+f)
        elif abs(zt-1) < p:
            fl[i] = 1 - f/(1+f)*(p**2*
                    arccos(min(max(-1,(zt**2+p**2-1)/(2*zt*p)),1)) + 
                    arccos(min(max(-1,(zt**2+1-p**2)/(2*zt)),1)) - 
                    0.5*sqrt(max(0,(1+p-zt)*(zt+p-1)*(zt-p+1)*(zt+p+1)))
                    ) /(pi*p**2)
    return fl
