import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2,2), 4)
        self.assertEqual(Calculator.add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 0), 10)
        self.assertEqual(Calculator.subtract(-3, -2), -1)
    
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 0), 0)
        self.assertEqual(Calculator.multiply(-3, -2), 6)
    
    def test_divide(self):
 #       self.assertRaises(ZeroDivisionError, Calculator.multiply, 10, 0)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)
        self.assertEqual(Calculator.divide(4, -2), -2)
