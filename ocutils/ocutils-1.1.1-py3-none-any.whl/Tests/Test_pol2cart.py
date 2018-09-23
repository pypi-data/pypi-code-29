'''
Test class for pol2cart function
'''

import unittest
import numpy
from ocutils.pol2cart import pol2cart


class Test_pol2cart(unittest.TestCase):

    def setUp(self):

        self.r = numpy.linspace(1, 10, 10)
        self.theta = numpy.linspace(0, 2 * numpy.pi, 9)
        nr = self.r.size
        ntheta = self.theta.size

        self.pol2D = numpy.zeros([ntheta, nr])
        for ti in range(ntheta):
            self.pol2D[ti] = ti * self.r

        nz = 3  # 3 element z axis
        self.pol3D = numpy.tile(self.pol2D, [3, 1, 1])
        for zi in range(nz):
            self.pol3D[zi] *= (zi + 1) * 2

        self.xmin = -2
        self.xmax = 5
        self.ymin = -7
        self.ymax = 3

        self.num_dp = 6  # Number of decimal places to check

    def tearDown(self):
        pass

    def test_axes(self):

        pxo = pyo = 0
        x_e = numpy.linspace(self.xmin, self.xmax, 8)  # Expected x coords
        y_e = numpy.linspace(self.ymin, self.ymax, 11)  # Expected y coords

        x, y, _ = pol2cart(self.r, self.theta, self.pol2D, pxo, pyo,
                           self.xmin, self.xmax, self.ymin, self.ymax)

        self.assertTrue(numpy.array_equal(x, x_e))
        self.assertTrue(numpy.array_equal(y, y_e))

    def test_2D(self):

        pxo = pyo = 0
        _, _, cart = pol2cart(self.r, self.theta, self.pol2D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[2, 8], 0)  # x=0, y=1
        self.assertEqual(cart[7, 7], 2 * 5)  # x=5, y=0
        self.assertEqual(cart[3, 6],
                         numpy.around(3 * numpy.sqrt(2), self.num_dp))  # x=1, y=-1: r = sqrt(2)
        self.assertEqual(cart[0, 9],
                         numpy.around(7 * 2 * numpy.sqrt(2), self.num_dp))  # x=-2, y=2: r = 2*sqrt(2)

    def test_3D(self):

        pxo = pyo = 0
        _, _, cart = pol2cart(self.r, self.theta, self.pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 2, 10], 0)  # x=0, y=3
        self.assertEqual(cart[0, 6, 7], 2 * 2 * 4)  # x=4, y=0
        self.assertEqual(cart[1, 1, 8],
                         numpy.around(4 * 7 * numpy.sqrt(2), self.num_dp))  # x=-1, y=1: r = sqrt(2)
        self.assertEqual(cart[2, 4, 5],
                         numpy.around(6 * 3 * 2 * numpy.sqrt(2), self.num_dp))  # x=2, y=-2: r = 2*sqrt(2)

    def test_steps(self):

        pxo = pyo = 0
        xstep = 0.5
        ystep = 0.25
        _, _, cart = pol2cart(self.r, self.theta, self.pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax,
                              xstep=xstep, ystep=ystep)

        self.assertEqual(cart[0, 4, 36], 0)  # x=0, y=2
        self.assertEqual(cart[-1, 2, 28], 6 * 6)  # x=-1, y=0

    def test_offset(self):

        pxo = 1
        pyo = -1
        _, _, cart = pol2cart(self.r, self.theta, self.pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 2, 7],
                         numpy.around(2 * 7 * numpy.sqrt(2), self.num_dp))  # x=0, y=0, r = sqrt(2)
        self.assertEqual(cart[-1, -1, -1],
                         numpy.around(6 * 4 * numpy.sqrt(2), self.num_dp))  # x=5, y=3, r = 4*sqrt(2)

    def test_nan(self):

        pxo = pyo = 0
        _, _, cart = pol2cart(self.r, self.theta, self.pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)

        self.assertTrue(numpy.isnan(cart[0, 2, 7]))
        self.assertTrue(numpy.isnan(cart[-1, 2, 7]))

    def test_sector(self):

        pxo = pyo = 0

        theta = self.theta[1:5]  # 45 to 180 degrees
        pol3D = self.pol3D[:, 1:5, :]

        _, _, cart = pol2cart(self.r, theta, pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 6, 7], 2 * 2 * 4)  # x=4, y=0
        self.assertEqual(cart[2, 4, 5],
                         numpy.around(6 * 3 * 2 * numpy.sqrt(2), self.num_dp))  # x=2, y=-2: r = 2*sqrt(2)

    def test_negative_theta_2D(self):

        pxo = pyo = 0
        theta = self.theta - numpy.pi
        pol2D = self.pol2D[:-1].copy()
        pol2D = numpy.roll(pol2D, 4, axis=0)
        pol2D = numpy.append(pol2D, pol2D[0:1, :], axis=0)
        _, _, cart = pol2cart(self.r, theta, pol2D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[2, 8], 0)  # x=0, y=1
        self.assertEqual(cart[7, 7], 2 * 5)  # x=5, y=0
        self.assertEqual(cart[3, 6],
                         numpy.around(3 * numpy.sqrt(2), self.num_dp))  # x=1, y=-1: r = sqrt(2)
        self.assertEqual(cart[0, 9],
                         numpy.around(7 * 2 * numpy.sqrt(2), self.num_dp))  # x=-2, y=2: r = 2*sqrt(2)

    def test_negative_theta_3D(self):

        pxo = pyo = 0
        theta = self.theta - numpy.pi
        pol3D = self.pol3D[:, :-1].copy()
        pol3D = numpy.roll(pol3D, 4, axis=1)
        pol3D = numpy.append(pol3D, pol3D[:, 0:1, :], axis=1)
        _, _, cart = pol2cart(self.r, theta, pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 2, 10], 0)  # x=0, y=3
        self.assertEqual(cart[0, 6, 7], 2 * 2 * 4)  # x=4, y=0
        self.assertEqual(cart[1, 1, 8],
                         numpy.around(4 * 7 * numpy.sqrt(2), self.num_dp))  # x=-1, y=1: r = sqrt(2)
        self.assertEqual(cart[2, 4, 5],
                         numpy.around(6 * 3 * 2 * numpy.sqrt(2), self.num_dp))  # x=2, y=-2: r = 2*sqrt(2)

    def test_offset_negative_theta(self):

        pxo = 1
        pyo = -1
        theta = self.theta - numpy.pi
        pol3D = self.pol3D[:, :-1].copy()
        pol3D = numpy.roll(pol3D, 4, axis=1)
        pol3D = numpy.append(pol3D, pol3D[:, 0:1, :], axis=1)
        _, _, cart = pol2cart(self.r, theta, pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 2, 7],
                         numpy.around(2 * 7 * numpy.sqrt(2), self.num_dp))  # x=0, y=0, r = sqrt(2)
        self.assertEqual(cart[-1, -1, -1],
                         numpy.around(6 * 4 * numpy.sqrt(2), self.num_dp))  # x=5, y=3, r = 4*sqrt(2)

    def test_sector_negative_theta(self):

        pxo = pyo = 0

        theta = self.theta - numpy.pi
        pol3D = self.pol3D[:, :-1].copy()
        pol3D = numpy.roll(pol3D, 4, axis=1)
        pol3D = numpy.append(pol3D, pol3D[:, 0:1, :], axis=1)

        theta = theta[3:6]  # -45 to 45 degrees
        pol3D = pol3D[:, 3:6, :]

        _, _, cart = pol2cart(self.r, theta, pol3D, pxo, pyo,
                              self.xmin, self.xmax, self.ymin, self.ymax)
        cart = numpy.around(cart, self.num_dp)

        self.assertEqual(cart[0, 2, 10], 0)  # x=0, y=3

if __name__ == '__main__':
    unittest.main()
