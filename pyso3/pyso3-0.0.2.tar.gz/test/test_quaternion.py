import unittest

class TestQuaternion(unittest.TestCase):
    def test_trivial(self):
        import numpy as np
        from pyso3 import quat2rot
        q = np.zeros(4)
        q[0] = 1.0
        R = quat2rot(q)
        delta = R - np.eye(3)
        err = max(abs(delta.flatten()))
        self.assertAlmostEqual(err, 0.0, places=6)

    def test_random(self):
        import numpy as np
        from pyso3 import quat2rot, rot2quat
        q = np.random.randn(4)
        q = q / np.linalg.norm(q)
        R = quat2rot(q)
        from pyso3.check import isSO
        self.assertTrue(isSO(R))
        q2 = rot2quat(R)
        err = max(abs((q2-q).flatten()))
        self.assertAlmostEqual(err,0.0)

if __name__ == '__main__':
    unittest.main()
