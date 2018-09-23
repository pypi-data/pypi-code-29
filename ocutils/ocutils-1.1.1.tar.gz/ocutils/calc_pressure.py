'''
Pressure calculator function.

The pressure is calculated from input depth and latitude using the National Physical Laboratory (NPL)
online technical guide at http://resource.npl.co.uk/acoustics/techguides/soundseawater/content.html
NB: The Leroy-Parthiot corrections are not currently implemented, hence the output is slightly different
from the NPL online calculator

The inputs are NumPy 1D arrays of depth (m) and latitude (degrees), and a flag to apply the Leroy and Parthiot
correction for common oceans.

Returns a pressure array (bar) of dimensions depth, latitude
'''

import numpy


def calc_pressure(z, lat, do_corr=True):

    dr = numpy.pi / 180  # Deg to rad conversion

    nd = z.size
    nlat = lat.size

    zmat = numpy.tile(z, [nlat, 1]).T

    h0 = 1e-2 * z / (z + 100) + 6.2e-6 * z
    h0mat = numpy.tile(h0, [nlat, 1]).T

    g = 9.7803 * (1 + 5.3e-3 * numpy.sin(lat * dr)**2)
    gmat = numpy.tile(g, [nd, 1])

    k = (gmat - 2e-5 * zmat) / (9.80612 - 2e-5 * zmat)

    h45 = 1.00818 * 1e-2 * z + 2.465 * 1e-8 * z**2 - 1.25 * 1e-13 * z**3 + 2.8e-19 * z**4
    h45mat = numpy.tile(h45, [nlat, 1]).T

    hphi = h45mat * k

    P = hphi
    if do_corr:
        P -= h0mat

    P *= 10  # Convert from MPa to bar

    return P
