# https://github.com/KhaleelA19/lab10-KA-CL.git
# Partner 1: Khaleel Abiru
# Partner 2: Camila Lipson

import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(mul(1,2), 2)
        self.assertAlmostEqual(mul(1.1,2), 2.2)
        self.assertAlmostEqual(mul(-1,2), -2)
    def test_divide(self):
        self.assertEqual(div(4,2), 0.5)
        self.assertAlmostEqual(div(5,2.5), 0.5)
        self.assertAlmostEqual(div(-4.2,-2.1), 0.5)
        with self.assertRaises(ZeroDivisionError): div(0,2)
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

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(3, 3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 1/3)
        self.assertAlmostEqual(logarithm(100, 10), 0.5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, -2)
        with self.assertRaises(ValueError):
            logarithm(10, 0)



if __name__ == '__main__':
    unittest.main()