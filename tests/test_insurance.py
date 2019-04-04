import unittest
from kosimpletax.y2018 import tax_calculator
'''
4대보험 테스트, 근로자 부담액
보험료는 비과세 금액 제외 기준
월 급여액이 250만원(비과세소득과 과세되는 학자금 제외)인 경우
국민연금의 경우 월 급여액 구간 2500천원 ~ 2510천원의 중간값으로 계산함(천원미만 절사)
'''
class InsuranceTest(unittest.TestCase):
	def test_health_insurance(self):
		calc = tax_calculator.Calculator()
		insure = calc.health_insurance(2500000)
		self.assertEqual(insure, 80750.0)

	def test_long_term_insurance(self):
		calc = tax_calculator.Calculator()
		result = calc.long_term_insurance(2500000)
		self.assertEqual(result, 6870.0)

	def test_national_pension(self):
		calc = tax_calculator.Calculator()
		result = calc.national_pension(2500000)
		self.assertEqual(result, 112720.0)

	def test_employment_insurance(self):
		calc = tax_calculator.Calculator()
		result = calc.employment_insurance(2500000)
		self.assertEqual(result, 16250.0)		