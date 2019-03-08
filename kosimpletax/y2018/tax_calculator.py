import formula

class calculator():

	def __init__(self, salary, unit='WON'):
		self.salary = salary
		self.unit = unit

	def get_simple_tax_amount():
		print("연간 총급여액: {}".format(self.salary))
		earned_income_deduction = calc_earned_income_deduction(self.salary)
		print("근로소득공제: {}".format(earned_income_deduction))
		earned_income_amount = calc_earned_income_amount(self.salary, earned_income_deduction)
		print("근로소득금액: {}".format(earned_income_amount))
		personal_allowance = calc_personal_allowance(number_of_people)
		print("인적공제: {}".format(personal_allowance))
		annuity_insurance = calc_annuity_insurance_deduction(self.salary)
		print("연금보험료공제: {}".format(annuity_insurance))
		special_income_deduction = calc_special_income_deduction(self.salary, number_of_people)
		print("특별 소득공제: {}".format(special_income_deduction))
		tax_base = calc_tax_base(earned_income_amount, personal_allowance, annuity_insurance, special_income_deduction)
		print("과세표준: {}".format(tax_base))
		tax_assessment = calc_tax_assessment(tax_base)
		print("산출세액: {}".format(tax_assessment))
		tax_credit = calc_earned_income_tax_credit(tax_assessment, self.salary)
		print("근로소득 세액공제: {}".format(tax_credit))
		finalized_tax_amount = calc_finalized_tax_amount(tax_assessment, tax_credit)
		print("결정세액: {}".format(finalized_tax_amount))
		simplicity_tax_amount = calc_ease_tax_amount(finalized_tax_amount)
		print("간이세액: {}".format(simplicity_tax_amount))
		return simplicity_tax_amount