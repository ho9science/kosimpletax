from kosimpletax.y2018 import formula

class Calculator():

	def __init__(self, unit='WON', number_of_family_dependent=1, number_of_less_than_twenty=0):
		self.unit = unit
		self.number_of_family_dependent = number_of_family_dependent
		self.number_of_less_than_twenty = number_of_less_than_twenty

	def set_unit(self, unit):
		self.unit = unit

	def set_number_of_family_dependent(self, number_of_family_dependent):
		self.number_of_family_dependent = number_of_family_dependent

	def set_number_of_less_than_twenty(self, number_of_less_than_twenty):
		self.number_of_less_than_twenty = number_of_less_than_twenty

	def get_total_annual_income(self, income):
		return formula.calc_total_annual_income(income)

	def get_earned_income_deduction(self, salary):
		annual_income = self.get_total_annual_income(salary)
		return formula.calc_earned_income_deduction(annual_income)

	def get_earned_income_amount(self, salary):
		earned_income_deduction = self.get_earned_income_deduction(salary)
		return formula.calc_earned_income_amount(salary, earned_income_deduction)
		
	def get_personal_allowance(self):
		return formula.calc_personal_allowance(self.number_of_family_dependent, self.number_of_less_than_twenty)

	def get_annuity_insurance_deduction(self, salary):
		return formula.calc_annuity_insurance_deduction(salary)

	def get_special_income_deduction(self, salary):
		return formula.calc_special_income_deduction(salary, self.number_of_family_dependent)

	def get_tax_base(self, salary):
		earned_income_deduction = self.get_earned_income_deduction(salary)
		earned_income_amount = self.get_earned_income_amount(salary)
		personal_allowance = self.get_personal_allowance()
		annuity_insurance = self.get_annuity_insurance_deduction(salary)
		special_income_deduction = self.get_special_income_deduction(salary)
		return formula.calc_tax_base(earned_income_amount, personal_allowance, annuity_insurance, special_income_deduction)

	def get_tax_assessment(self, salary):
		tax_base = self.get_tax_base(salary)
		return formula.calc_tax_assessment(tax_base)

	def get_tax_credit(self, tax_assessment, salary):
		return formula.calc_earned_income_tax_credit(tax_assessment, salary)

	def get_finalized_tax_amount(self, salary):
		tax_assessment = self.get_tax_assessment(salary)
		tax_credit = self.get_tax_credit(tax_assessment, salary)
		return formula.calc_finalized_tax_amount(tax_assessment, tax_credit)

	def get_simple_tax_amount(self, income):
		salary = self.get_total_annual_income(income)
		finalized_tax_amount = self.get_finalized_tax_amount(salary)
		return formula.calc_ease_tax_amount(finalized_tax_amount)
		