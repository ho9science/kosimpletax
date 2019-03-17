from kosimpletax.y2018 import formula

class Calculator():

	def __init__(self, unit='WON'):
		self.unit = unit


	def get_simple_tax_amount(self, income, number_of_people=1):
		# salary = calc_total_annual_income(2505000, 'monthly')
		salary = formula.calc_total_annual_income(income)
		earned_income_deduction = formula.calc_earned_income_deduction(salary)
		earned_income_amount = formula.calc_earned_income_amount(salary, earned_income_deduction)
		personal_allowance = formula.calc_personal_allowance(number_of_people)
		annuity_insurance = formula.calc_annuity_insurance_deduction(salary)
		special_income_deduction = formula.calc_special_income_deduction(salary, number_of_people)
		tax_base = formula.calc_tax_base(earned_income_amount, personal_allowance, annuity_insurance, special_income_deduction)
		tax_assessment = formula.calc_tax_assessment(tax_base)
		tax_credit = formula.calc_earned_income_tax_credit(tax_assessment, salary)
		finalized_tax_amount = formula.calc_finalized_tax_amount(tax_assessment, tax_credit)
		simplicity_tax_amount = formula.calc_ease_tax_amount(finalized_tax_amount)
		return simplicity_tax_amount