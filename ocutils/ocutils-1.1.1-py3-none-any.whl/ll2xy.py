'''ll2xy function definition'''

import numpy
from ocutils import earth_radius


def ll2xy(lat, lon, latc, lonc):

    '''
    Convert from latitude and longitude to Cartesian coordinates using a flat Earth approximation.
    Inputs...
        lat: latitude (degrees), single value or NumPy array
        lon: longitude (degrees), single value or NumPy array
        latc: central latitude (degrees)
        lonc: central longitude (degrees)
    Returns...
        x: Cartesian x coordinate (m), same type as lon
        y: Cartesian y coordinate (m), same type as lat
    '''

    y = earth_radius * numpy.deg2rad(lat - latc)
    x = earth_radius * numpy.cos(numpy.deg2rad(latc)) * numpy.deg2rad(lon - lonc)

    return x, y
