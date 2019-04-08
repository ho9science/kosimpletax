import unittest
from kosimpletax.y2018 import tax_calculator
'''
실수령액은 
비과세 금액을 제외한 금액으로 4대보험을 계산하고 그 금액을 제한 후 소득세와 지방소득세를 제하여 계산합니다.
'''
class RealSalaryTest(unittest.TestCase):
	def test_after_tax_income(self):
		calc = tax_calculator.Calculator()
		insure = calc.after_tax_income(2500000)
		self.assertEqual(insure, 2292065.0)

			