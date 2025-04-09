import unittest
import math

from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(1,2), 2)
        self.assertAlmostEqual(multiply(1.1,2), 2.2)
        self.assertAlmostEqual(multiply(-1,2), -2)
    def test_divide(self):
        self.assertEqual(divide(4,2), 2)
        self.assertAlmostEqual(divide(5,2.5), 2.0)
        self.assertAlmostEqual(divide(-4.2,-2.1), 2.0)
        with self.assertRaises(ZeroDivisionError): divide(0,2)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(1, 2)
        with self.assertRaises(ValueError):
            logarithm(-1, 2)
        with self.assertRaises(ValueError):
            logarithm(0, 2)
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5.0)
        self.assertEqual(hypotenuse(-3,4), 5.0)
    def test_sqrt(self):
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(2),math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == '__main__':
    unittest.main()