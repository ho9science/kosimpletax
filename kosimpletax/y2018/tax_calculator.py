from kosimpletax.y2018 import formula

class Calculator():

	def __init__(self, unit='WON', number_of_family_dependent=1, number_of_less_than_twenty=0, exemption=100000):
		self.unit = unit
		self.family_dependent = number_of_family_dependent
		self.less_than_twenty = number_of_less_than_twenty
		self.exemption = exemption

	def set_unit(self, unit):
		self.unit = unit

	def set_family_dependent(self, number_of_family_dependent):
		self.family_dependent = number_of_family_dependent

	def set_less_than_twenty(self, number_of_less_than_twenty):
		self.less_than_twenty = number_of_less_than_twenty

	def set_exemption(self, exemption):
		self.exemption = exemption

	def get_total_annual_income(self, income):
		return formula.calc_total_annual_income(income)

	def get_total_monthly_income(self, income):
		return formula.calc_total_monthly_income(income)

	def get_earned_income_deduction(self, annual_income):
		return formula.calc_earned_income_deduction(annual_income)

	def get_earned_income_amount(self, salary):
		earned_income_deduction = self.get_earned_income_deduction(salary)
		return formula.calc_earned_income_amount(salary, earned_income_deduction)
		
	def get_personal_allowance(self):
		return formula.calc_personal_allowance(self.family_dependent, self.less_than_twenty)

	def get_annuity_insurance_deduction(self, salary):
		return formula.calc_annuity_insurance_deduction(salary)

	def get_special_income_deduction(self, salary):
		return formula.calc_special_income_deduction(salary, self.family_dependent)

	def get_tax_base(self, salary):
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

	def earned_income_tax(self, income, time='monthly'):
		if time == 'year':
			salary = self.get_total_annual_income(income)
		else:
			salary = self.get_total_monthly_income(income) * 12
		finalized_tax_amount = self.get_finalized_tax_amount(salary)
		return formula.calc_ease_tax_amount(finalized_tax_amount)

	def local_income_tax(self, simple_tax):
		local_income_tax = simple_tax * 0.1
		return local_income_tax - local_income_tax % 10
	#80% 100% 120%추가
	def simple_tax(self, salary):
		tax = self.earned_income_tax(income)
		local_tax = self.local_income_tax(tax)
		return tax+local_tax

	def national_pension(self, income, time='monthly'):
		if time == 'year':
			salary = self.get_total_annual_income(income)
			return formula.calc_national_pension(salary)
		else:
			salary = self.get_total_monthly_income(income)
			return formula.calc_national_pension(salary)

	def health_insurance(self, monthly_salary):
		return formula.calc_health_insurance(monthly_salary) * 0.5

	def long_term_insurance(self, monthly_salary):
		health_insurance = formula.calc_health_insurance(monthly_salary)
		return formula.calc_long_term_insurance(health_insurance) * 0.5

	def employment_insurance(self, monthly_salary):
		return formula.calc_employment_insurance(monthly_salary)

	def tax_exemption(self, salary):
		if salary > self.exemption:
			return salary - self.exemption
		else:
			print('비과세 금액 보다 월급여액이 적습니다.')

	def after_tax_income(self, salary):
		salary = self.tax_exemption(salary)
		pension_amount = self.national_pension(salary)
		insure_amount = self.health_insurance(salary)
		long_term_amount = self.long_term_insurance(salary)
		employ_amount = self.employment_insurance(salary)
		return salary - pension_amount - insure_amount - long_term_amount - employ_amount + self.exemption
	
	def all_tax_income(self, salary):
		criteria = {}
		origin_salary = salary
		salary = self.tax_exemption(salary)
		pension_amount = self.national_pension(salary)
		insure_amount = self.health_insurance(salary)
		long_term_amount = self.long_term_insurance(salary)
		employment_amount = self.employment_insurance(salary)
		tax = self.earned_income_tax(salary)
		local_tax = self.local_income_tax(tax)
		real_income = salary - pension_amount - insure_amount - long_term_amount - employ_amount - tax - local_tax + self.exemption
		criteria['exemption'] = self.exemption
		criteria['origin_salary'] = origin_salary
		criteria['pension'] = pension_amount
		criteria['insure'] = insure_amount
		criteria['long_term'] = long_term_amount
		criteria['employment'] = employment_amount
		criteria['tax'] = tax
		criteria['local_tax'] = local_tax
		criteria['real_salary'] = real_income
		return criteria