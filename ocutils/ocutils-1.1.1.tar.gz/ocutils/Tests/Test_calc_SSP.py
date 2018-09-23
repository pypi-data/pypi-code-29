'''
Test class for calc_SSP function

The test values below were taken from the NPL online calculator at:
http://resource.npl.co.uk/acoustics/techguides/soundseawater/content.html
'''

import unittest
import numpy
from ocutils.calc_SSP import calc_SSP
from ocutils.get_path import get_path


class Test_calc_SSP(unittest.TestCase):

    def setUp(self):
        # Define the test values
        self.T = numpy.array([0, 20, 40])  # Temperature (degrees Celsius)
        self.S = numpy.array([35, 0, 40])  # Salinity (ppt)
        self.P = numpy.array([1, 10, 50])  # Pressure (bar)
        self.c_NPL = numpy.array([1449.301192, 1484.009915, 1576.575496])  # Values from online NPL calculator to 6 d.p. (taken on 7/1/16)
        self.num_dp = 6  # Number of decimal places kept from NPL values
        self.coeffs_file = get_path('CM_coeffs.txt')

    def tearDown(self):
        pass

    def test_SSP_calculation(self):
        c = numpy.zeros(3)
        Tin = numpy.zeros([1, 1, 1, 1])
        Sin = numpy.zeros([1, 1, 1, 1])
        Pin = numpy.zeros([1, 1])
        for n in range(c.size):
            Tin[:] = self.T[n]
            Sin[:] = self.S[n]
            Pin[:] = self.P[n]
            c[n] = calc_SSP(Sin, Tin, Pin, self.coeffs_file)
        c = numpy.around(c, decimals=self.num_dp)
        self.assertTrue(numpy.array_equal(c, self.c_NPL))


if __name__ == '__main__':
    unittest.main()
