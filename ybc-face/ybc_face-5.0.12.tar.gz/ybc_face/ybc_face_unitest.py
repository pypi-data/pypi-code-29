import unittest
from ybc_face import *


class MyTestCase(unittest.TestCase):
    def test_gender(self):
        self.assertEqual('男', gender('test.jpg'))


    def test_glass(self):
        self.assertEqual(True, glass('test.jpg'))


if __name__ == '__main__':
    unittest.main()
