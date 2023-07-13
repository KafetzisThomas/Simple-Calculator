import unittest
from main import Calculator

class CalculatorTestCase(unittest.TestCase):
  """Tests for 'main.py'"""
  
  def setUp(self):
    """Set up instance with initial values"""
    self.calculator = Calculator(5, 5)

  def test_addition(self):
    """Test if addition method is working"""
    self.assertEqual(self.calculator.addition(), 10)
    self.assertNotEqual(self.calculator.addition(), 0)
    self.assertNotEqual(self.calculator.addition(), 25)
    self.assertNotEqual(self.calculator.addition(), 1)

  def test_subtraction(self):
    """Test if subtraction method is working"""
    self.assertEqual(self.calculator.subtraction(), 0)
    self.assertNotEqual(self.calculator.subtraction(), 10)
    self.assertNotEqual(self.calculator.subtraction(), 25)
    self.assertNotEqual(self.calculator.subtraction(), 1)

  def test_multiplication(self):
    """Test if multiplication method is working"""
    self.assertEqual(self.calculator.multiplication(), 25)
    self.assertNotEqual(self.calculator.multiplication(), 10)
    self.assertNotEqual(self.calculator.multiplication(), 0)
    self.assertNotEqual(self.calculator.multiplication(), 1)

  def test_division(self):
    """Test if division method is working"""
    self.assertEqual(self.calculator.division(), 1)
    self.assertNotEqual(self.calculator.division(), 10)
    self.assertNotEqual(self.calculator.division(), 0)
    self.assertNotEqual(self.calculator.division(), 25)

if __name__ == '__main__':
  unittest.main()
