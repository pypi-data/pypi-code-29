'''
Test class for ll2xy function
'''

import unittest
import numpy
from ocutils import earth_radius
from ocutils.ll2xy import ll2xy


class Test_ll2xy(unittest.TestCase):

    def setUp(self):
        self.tol = 1e-6

    def tearDown(self):
        pass

    def test_single(self):

        latc = lonc = 0
        lat = 60
        lon = 90
        yt = earth_radius * numpy.pi / 3
        xt = earth_radius * numpy.pi / 2
        x, y = ll2xy(lat, lon, latc, lonc)
        self.assertTrue(numpy.abs(x - xt) <= self.tol)
        self.assertTrue(numpy.abs(y - yt) <= self.tol)

    def test_single_offs(self):

        latc = 60
        lonc = -30
        lat = 0
        lon = 30
        yt = -earth_radius * numpy.pi / 3
        xt = earth_radius * 0.5 * numpy.pi / 3
        x, y = ll2xy(lat, lon, latc, lonc)
        self.assertTrue(numpy.abs(x - xt) <= self.tol)
        self.assertTrue(numpy.abs(y - yt) <= self.tol)

    def test_multi(self):

        latc = lonc = 0
        lat = numpy.array([60., -60.])
        lon = numpy.array([-90., 90.])
        yt = earth_radius * numpy.pi / 3
        xt = earth_radius * numpy.pi / 2
        yta = numpy.array([yt, -yt])
        xta = numpy.array([-xt, xt])
        x, y = ll2xy(lat, lon, latc, lonc)
        self.assertTrue(numpy.abs(x - xta).mean() <= self.tol)
        self.assertTrue(numpy.abs(y - yta).mean() <= self.tol)

    def test_multi_offs(self):

        latc = 60
        lonc = 30
        lat = numpy.array([60., 0.])
        lon = numpy.array([-30., 30.])
        yt = earth_radius * numpy.pi / 3
        xt = earth_radius * 0.5 * numpy.pi / 3
        yta = numpy.array([0, -yt])
        xta = numpy.array([-xt, 0])
        x, y = ll2xy(lat, lon, latc, lonc)
        self.assertTrue(numpy.abs(x - xta).mean() <= self.tol)
        self.assertTrue(numpy.abs(y - yta).mean() <= self.tol)

if __name__ == '__main__':
    unittest.main()
