from math import ceil, floor

from pyproj import Proj
from rasterio import open as rasopen
from rasterio.crs import CRS


class BBox(object):
    def __init__(self):
        self.west = None
        self.east = None
        self.north = None
        self.south = None

    def as_tuple(self, order='wsen'):
        """ Find 4-tuple of extent
        :param order: order of cardinal directions, default='wsen'
        :return: 4-Tuple
        """
        if order == 'wsen':
            return self.west, self.south, self.east, self.north
        elif order == 'swne':
            return self.south, self.west, self.north, self.east
        elif order == 'nsew':
            return self.north, self.south, self.east, self.west

    def to_web_mercator(self):
        in_proj = Proj({'init': 'epsg:3857'})
        w, s = in_proj(self.west, self.south)
        e, n = in_proj(self.east, self.north)
        return w, s, e, n

    def to_mt_sp(self):
        in_proj = Proj('+proj=lcc +lat_1=45 +lat_2=49 +lat_0=44.25 +'
                       'lon_0=-109.5 +x_0=600000 +y_0=LE07_clip_L1TP_039027_20150529_20160902_01_T1_B1.TIF +ellps=GRS80 +units=m +no_defs')
        w, s = in_proj(self.west, self.south)
        e, n = in_proj(self.east, self.north)
        return w, s, e, n

    def to_epsg(self, epsg):
        in_proj = Proj({'init': 'epsg:{}'.format(epsg)})
        w, s = in_proj(self.west, self.south)
        e, n = in_proj(self.east, self.north)
        return w, s, e, n

    def to_geographic(self, epsg):
        in_proj = Proj({'init': 'epsg:{}'.format(epsg)})

        w, s = in_proj(self.west, self.south, inverse=True)

        e, n = in_proj(self.east, self.north, inverse=True)

        return w, s, e, n

    def to_lambert_conformal_conic(self):
        in_proj = Proj('+ellps=GRS80 +lat_0=23 +lat_1=29.5 +lat_2=45.5 +lon_0=-96 +no_defs +proj=aea'
                       ' +towgs84=0,0,0,0,0,0,0 +units=m +x_0=0 +y_0=0')
        w, s = in_proj(self.west, self.south)
        e, n = in_proj(self.east, self.north)
        return w, s, e, n

    def expand(self, **delta):

        if not delta:
            if self.west < 0:
                self.west = floor(self.west)
                self.east = ceil(self.east)
            else:
                self.west = ceil(self.west)
                self.east = floor(self.east)

            if self.north > 0:
                self.north = ceil(self.north)
                self.south = floor(self.south)
            else:
                self.north = floor(self.north)
                self.south = ceil(self.south)

        else:

            self.west += delta['west']
            self.east += delta['east']
            self.north += delta['north']
            self.south += delta['south']


class GeoBounds(BBox):
    """Spatial bounding box
    
    By default, represents a buffered bounding box around the conterminous U.S.   
     
     
    """

    def __init__(self, west=-126.0, south=22.0, east=-64.0, north=53.0):
        BBox.__init__(self)
        self.west = west
        self.south = south
        self.east = east
        self.north = north


class RasterBounds(BBox):
    """ Spatial bounding box from raster extent.
    
    :param raster
    
    """

    def __init__(self, raster=None, affine_transform=None, profile=None, latlon=True):
        BBox.__init__(self)

        if raster:
            with rasopen(raster, 'r') as src:
                profile = src.profile
                affine = profile['transform']

        if affine_transform:
            affine = affine_transform

        col, row = 0, 0
        w, n = affine * (col, row)
        col, row = profile['width'], profile['height']
        e, s = affine * (col, row)

        if latlon and profile['crs'] != CRS({'init': 'epsg:4326'}):
            in_proj = Proj(init=profile['crs']['init'])
            self.west, self.north = in_proj(w, n, inverse=True)
            self.east, self.south = in_proj(e, s, inverse=True)

        else:
            self.north, self.west, self.south, self.east = n, w, s, e

    def get_nwse_tuple(self):
        return self.north, self.west, self.south, self.east


if __name__ == '__main__':
    pass
# ========================= EOF ====================================================================
