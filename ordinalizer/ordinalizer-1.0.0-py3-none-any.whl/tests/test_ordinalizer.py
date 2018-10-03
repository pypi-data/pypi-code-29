import unittest
import ordinalizer.ordinalizer as ordinalizer


class TestOrdinalizer(unittest.TestCase):

    def test_up_to_21(self):
        test_parameters = [("1st", 1), ("2nd", 2), ("3rd", 3), ("4th", 4), ("5th", 5),
                           ("6th", 6), ("7th", 7), ("8th", 8), ("9th", 9), ("10th", 10),
                           ("11th", 11), ("12th", 12), ("13th", 13), ("14th", 14), ("15th", 15),
                           ("16th", 16), ("17th", 17), ("18th", 18), ("19th", 19), ("20th", 20),
                           ("21st", 21)]
        for expected_ordinal, input_cardinal in test_parameters:
            with self.subTest(name=input_cardinal):
                self.assertEqual(expected_ordinal, ordinalizer.ordinalize(input_cardinal))

    def test_91(self):
        self.assertEqual("91st", ordinalizer.ordinalize(91))

    def test_111(self):
        self.assertEqual("111th", ordinalizer.ordinalize(111))

    def test_812(self):
        self.assertEqual("812th", ordinalizer.ordinalize(812))

    def test_32832(self):
        self.assertEqual("32832nd", ordinalizer.ordinalize(32832))

    def test_113(self):
        self.assertEqual("113th", ordinalizer.ordinalize(113))

    def test_123(self):
        self.assertEqual("123rd", ordinalizer.ordinalize(123))

    def test_10000000(self):
        self.assertEqual("1000000th", ordinalizer.ordinalize(1000000))

    def test_0(self):
        self.assertEqual("0th", ordinalizer.ordinalize(0))

    def test_negative_raises(self):
        with self.assertRaises(ordinalizer.NonOrdinalizableException):
            ordinalizer.ordinalize(-42)

    def test_float_raises(self):
        with self.assertRaises(ordinalizer.NonOrdinalizableException):
            ordinalizer.ordinalize(3.14)

    def test_negativ_numeric_string_raises(self):
        with self.assertRaises(ordinalizer.NonOrdinalizableException):
            ordinalizer.ordinalize("-56")

    def test_psotive_numeric_string_is_transformable(self):
        self.assertEqual("56th", ordinalizer.ordinalize("56"))

    def test_string_raises(self):
        with self.assertRaises(ordinalizer.NonOrdinalizableException):
            ordinalizer.ordinalize("da")


if __name__ == '__main__':
    unittest.main()
