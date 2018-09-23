'''
Test class for xy2ll function
'''

import unittest
import numpy
from ocutils import earth_radius
from ocutils.xy2ll import xy2ll


class Test_xy2ll(unittest.TestCase):

    def setUp(self):
        self.tol = 1e-6

    def tearDown(self):
        pass

    def test_single(self):

        latc = lonc = 0
        y = earth_radius * numpy.pi / 3
        x = earth_radius * numpy.pi / 2
        latt = 60
        lont = 90
        lat, lon = xy2ll(x, y, latc, lonc)
        self.assertTrue(numpy.abs(lat - latt) <= self.tol)
        self.assertTrue(numpy.abs(lon - lont) <= self.tol)

    def test_single_offs(self):

        latc = 60
        lonc = -30
        y = -earth_radius * numpy.pi / 3
        x = earth_radius * 0.5 * numpy.pi / 3
        latt = 0
        lont = 30
        lat, lon = xy2ll(x, y, latc, lonc)
        self.assertTrue(numpy.abs(lat - latt) <= self.tol)
        self.assertTrue(numpy.abs(lon - lont) <= self.tol)

    def test_multi(self):

        latc = lonc = 0
        ys = earth_radius * numpy.pi / 3
        xs = earth_radius * numpy.pi / 2
        y = numpy.array([ys, -ys])
        x = numpy.array([-xs, xs])
        latt = numpy.array([60., -60.])
        lont = numpy.array([-90., 90.])
        lat, lon = xy2ll(x, y, latc, lonc)
        self.assertTrue(numpy.abs(lat - latt).mean() <= self.tol)
        self.assertTrue(numpy.abs(lon - lont).mean() <= self.tol)

    def test_multi_offs(self):

        latc = 60
        lonc = 30
        ys = earth_radius * numpy.pi / 3
        xs = earth_radius * 0.5 * numpy.pi / 3
        y = numpy.array([0, -ys])
        x = numpy.array([-xs, 0])
        latt = numpy.array([60., 0.])
        lont = numpy.array([-30., 30.])
        lat, lon = xy2ll(x, y, latc, lonc)
        self.assertTrue(numpy.abs(lat - latt).mean() <= self.tol)
        self.assertTrue(numpy.abs(lon - lont).mean() <= self.tol)

if __name__ == '__main__':
    unittest.main()
