import unittest

def inf_norm(M):
    return max(abs(M.flatten()))

class TestExp(unittest.TestCase):
    def test_trivial(self):
        from pyso3 import exp
        import numpy as np
        out = exp(np.zeros((3,3)))
        err = inf_norm(out-np.eye(3))
        self.assertAlmostEqual(err,0,places=6)

    def test_180(self):
        from pyso3 import exp
        import numpy as np
        omega = np.zeros((3,3))
        omega[0,1] = np.pi
        omega = omega - omega.transpose()
        out = exp(omega)
        expected = np.eye(3)
        expected[0,0] = -1.0
        expected[1,1] = -1.0
        err = inf_norm(out-expected)
        self.assertAlmostEqual(err,0,places=6)

    def test_90(self):
        from pyso3 import exp
        import numpy as np
        omega = np.zeros((3,3))
        omega[0,1] = -np.pi / 2
        omega = omega - omega.transpose()
        out = exp(omega)
        expected = np.zeros((3,3))
        expected[0,1] = -1.0
        expected[1,0] = 1.0
        expected[2,2] = 1.0
        err = inf_norm(out-expected)
        self.assertAlmostEqual(err,0,places=6)

    def test_random_large(self):
        from pyso3 import exp
        import numpy as np
        omega = np.random.randn(3,3)*1000.0
        omega = omega - omega.transpose()
        out = exp(omega)
        from pyso3.check import isSO
        self.assertTrue(isSO(out))

class TestLog(unittest.TestCase):
    def test_log_inverts_exp(self):
        from pyso3 import exp, log
        import numpy as np
        omega = np.random.rand(3,3)
        omega = (omega - omega.transpose())/2.0
        R = exp(omega)
        omega_comp = log(R)
        err = inf_norm(omega-omega_comp)

if __name__ == '__main__':
    unittest.main()
