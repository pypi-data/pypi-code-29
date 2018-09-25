import unittest

class TestGenerate(unittest.TestCase):
    def test_generate(self):
        from pyso3 import generate_random_rot
        R = generate_random_rot()
        from pyso3.check import isSO
        self.assertTrue(isSO(R))

if __name__ == '__main__':
    unittest.main()
