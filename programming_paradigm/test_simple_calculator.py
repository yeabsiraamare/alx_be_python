import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3, 0), 3)
        self.assertEqual(self.calc.add(-10,-5), -15)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,2),8)
        self.assertEqual(self.calc.subtract(-5,5),0)
        self.assertEqual(self.calc.subtract(0,3),-3)
        self.assertEqual(self.calc.subtract(3,0),3)
        self.assertEqual(self.calc.subtract(-3,-5),-8)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,2),10)
        self.assertEqual(self.calc.multiply(5,0),0)
        self.assertEqual(self.calc.multiply(-6,2),-12)
        self.assertEqual(self.calc.multiply(-7,-3),21)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(0,4),0)
        self.assertEqual(self.calc.divide(8,0),None)
        self.assertEqual(self.calc.divide(10,-2),-5)
        self.assertEqual(self.calc.divide(-10,-2),5)