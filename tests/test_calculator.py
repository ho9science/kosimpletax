import unittest
from kosimpletax.y2018 import tax_calculator

class CalculatorTest(unittest.TestCase):
	def test_simple_tax_amount(self):
		calc = tax_calculator.Calculator()
		result = calc.get_simple_tax_amount(25000000)
		self.assertEqual(result, 22040.0)

if __name__ == '__main__':
	unittest.main()