import unittest
from kosimpletax.y2018 import tax_calculator

'''
근로소득 간이세액표 산출사례
연급여액(비과세소득과 과세되는 학자금 제외)을 파라미터로 넣고
공제대상을 정한다(20세미만 자녀는 추가로 입력)
'''
class CalculatorTest(unittest.TestCase):
	def test_simple_tax_calculation_example_first(self):
		calc = tax_calculator.Calculator()
		result = calc.earned_income_tax(30060000,'year')
		self.assertEqual(result, 41630.0)

	def test_simple_tax_calculation_example_second(self):
		calc = tax_calculator.Calculator()
		calc.set_family_dependent(4)
		calc.set_less_than_twenty(2)
		result = calc.earned_income_tax(48120000,'year')
		self.assertEqual(result, 75920.0)

	def test_simple_tax_calculation_example_third(self):
		calc = tax_calculator.Calculator()
		calc.set_family_dependent(2)
		result = calc.earned_income_tax(17970000,'year')
		self.assertEqual(result, 4260.0)

	def test_simple_tax_calculation_example_forth(self):
		calc = tax_calculator.Calculator()
		calc.set_family_dependent(5)
		calc.set_less_than_twenty(3)
		result = calc.earned_income_tax(5010000)
		self.assertEqual(result, 159100.0)


if __name__ == '__main__':
	unittest.main()