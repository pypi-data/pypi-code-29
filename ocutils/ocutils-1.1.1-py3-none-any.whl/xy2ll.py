'''xy2ll function definition'''

import numpy
from ocutils import earth_radius


def xy2ll(x, y, latc, lonc):

    '''
    Convert from Cartesian coordinates to latitude and longitude using a flat Earth approximation.
    Inputs...
        x: Cartesian x coordinate (m), single value or NumPy array
        y: Cartesian y coordinate (m), single value or NumPy array
        latc: central latitude (degrees)
        lonc: central longitude (degrees)
    Returns...
        lat: latitude (degrees), same type as y
        lon: longitude (degrees), same type as x
    '''

    lat = latc + numpy.rad2deg(y / earth_radius)
    lon = lonc + numpy.rad2deg(x / (earth_radius * numpy.cos(numpy.deg2rad(latc))))

    return lat, lon
