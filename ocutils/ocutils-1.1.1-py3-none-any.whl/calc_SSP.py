'''
Sound Speed Profile (SSP) calculator function.

The SSP is calculated from input temperature, salinity and pressure using the UNESCO (Chen & Millero) equation,
as provided in the National Physical Laboratory (NPL) online technical guide at:
http://resource.npl.co.uk/acoustics/techguides/soundseawater/content.html

The inputs are NumPy 4D arrays of temperature (degrees Celsius) and salinity (ppt) and a 2D pressure (bar) array

Temperature and salinity array dimensions are: time, depth, lat, long
Pressure array dimensions are: depth, lat

Returns a SSP array of same dimensions as T and S
'''

from ocutils.load_CM_coeffs import load_CM_coeffs
import numpy


def calc_SSP(S, T, P, coeffs_file):

    R = load_CM_coeffs(coeffs_file)  # Load the coefficients dictionary

    C = numpy.zeros(T.shape)

    nt, nd, _, nlon = T.shape

    for t in range(nt):  # Loop over time

        for d in range(nd):  # Loop over depth

            # Get pressure matrix and calculate powers

            pmat = numpy.tile(P[d], [nlon, 1]).T  # Pressure versus lat and long (invariant with long)
            pmat2 = pmat**2
            pmat3 = pmat**3

            # Get T and S matrices and calculate powers

            tmat = T[t, d]
            tmat2 = tmat**2
            tmat3 = tmat**3
            tmat4 = tmat**4
            tmat5 = tmat**5

            smat = S[t, d]
            smat3_2 = smat**(3 / 2)
            smat2 = smat**2

            # Calculate components

            Cw = R['C00'] + R['C01'] * tmat + R['C02'] * tmat2 + R['C03'] * tmat3 + R['C04'] * tmat4 + R['C05'] * tmat5 + \
                (R['C10'] + R['C11'] * tmat + R['C12'] * tmat2 + R['C13'] * tmat3 + R['C14'] * tmat4) * pmat + \
                (R['C20'] + R['C21'] * tmat + R['C22'] * tmat2 + R['C23'] * tmat3 + R['C24'] * tmat4) * pmat2 + \
                (R['C30'] + R['C31'] * tmat + R['C32'] * tmat2) * pmat3

            A = R['A00'] + R['A01'] * tmat + R['A02'] * tmat2 + R['A03'] * tmat3 + R['A04'] * tmat4 + \
                (R['A10'] + R['A11'] * tmat + R['A12'] * tmat2 + R['A13'] * tmat3 + R['A14'] * tmat4) * pmat + \
                (R['A20'] + R['A21'] * tmat + R['A22'] * tmat2 + R['A23'] * tmat3) * pmat2 + \
                (R['A30'] + R['A31'] * tmat + R['A32'] * tmat2) * pmat3

            B = R['B00'] + R['B01'] * tmat + (R['B10'] + R['B11'] * tmat) * pmat

            D = R['D00'] + R['D10'] * pmat

            # Calculate sound speed

            C[t, d] = Cw + A * smat + B * smat3_2 + D * smat2

    return C
