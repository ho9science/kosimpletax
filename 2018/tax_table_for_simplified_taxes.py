MANWON = 10000
def calc_total_annual_income(income, mothly=None):
	if mothly:
		salary = income * 12
	else:
		salary = income
	return salary

#근로소득공제
def calc_earned_income_deduction(salary):
	if salary <= 500*MANWON:
		amount_deducted = salary * 0.7
	elif salary <= 1500*MANWON:
		amount_deducted = 350*MANWON + ((salary-500*MANWON) * 0.4)
	elif salary <= 4500*MANWON:
		amount_deducted = 750*MANWON + ((salary-1500*MANWON) * 0.15)
	elif salary <= 10000*MANWON:
		amount_deducted = 1200*MANWON + ((salary-4500*MANWON) * 0.05)
	elif salary > 10000*MANWON:
		amount_deducted = 1475*MANWON + ((salary-10000*MANWON) * 0.02)
	return amount_deducted

#근로소득금액
def calc_earned_income_amount(salary, amount_deducted):
	earned_income_amount = salary - amount_deducted
	return earned_income_amount;

#인적공제
def calc_personal_allowance(number_of_people = 1):
	return number_of_people * 150*MANWON

#연금보험료공제
def calc_annuity_insurance_deduction(salary):
	#월급여액(비과세소득 제외)이 속한 구간의 중간 값(천원미만 절사) 필요
	annuity_insurance_amount = salary/12/1000*1000*0.045*12
	if annuity_insurance_amount < 15.66*MANWON:
		annuity_insurance_amount = 15.66*MANWON
	elif annuity_insurance_amount > 242.46*MANWON:
		annuity_insurance_amount = 242.46*MANWON
	return annuity_insurance_amount

#특별소득공제
def special_exemption_one(salary):
	if salary <= 3000*MANWON:
		return 310*MANWON + salary*0.04
	elif salary <= 4500*MANWON:
		return 310*MANWON + (salary*0.04) - ((salary-3000*MANWON) * 0.05)
	elif salary <= 7000*MANWON:
		return 310*MANWON + (salary*0.015)
	elif salary <= 12000*MANWON:	
		return 310*MANWON + (salary*0.005)

def special_exemption_two(salary):
	if salary <= 3000*MANWON:
		return 360*MANWON + salary*0.04
	elif salary <= 4500*MANWON:
		return 360*MANWON + (salary*0.04) - ((salary-3000*MANWON) * 0.05)
	elif salary <= 7000*MANWON:
		return 360*MANWON + (salary*0.02)
	elif salary <= 12000*MANWON:	
		return 360*MANWON + (salary*0.01)

def special_exemption_multiple(salary):
	additional_exemption = (salary - 4000*MANWON) * 0.04
	if salary <= 3000*MANWON:
		return 500*MANWON + salary*0.07 + additional_exemption
	elif salary <= 4500*MANWON:
		return 500*MANWON + (salary*0.07) - ((salary-3000*MANWON) * 0.05) + additional_exemption
	elif salary <= 7000*MANWON:
		return 500*MANWON + (salary*0.05) + additional_exemption
	elif salary <= 12000*MANWON:	
		return 500*MANWON + (salary*0.03) + additional_exemption

def calc_special_income_deduction(salary, number_of_people = 1):
	if number_of_people == 1:
		return special_exemption_one(salary)
	elif number_of_people == 2:
		return special_exemption_two(salary)
	elif number_of_people >= 3:
		return special_exemption_multiple(salary)

#과세표준
def calc_tax_base(earned_income, personal_allowance, annuity_insurance, special_exemption):
	return earned_income - personal_allowance - annuity_insurance - special_exemption

#산출세액
def calc_tax_assessment(tax_base):
	if tax_base <= 1200*MANWON:
		return tax_base*0.06
	elif tax_base <= 4600*MANWON:
		return 72*MANWON + (tax_base - 1200*MANWON)*0.15
	elif tax_base <= 8800*MANWON:
		return 582*MANWON + (tax_base - 4600*MANWON)*0.24
	elif tax_base <= 15000*MANWON:
		return 1590*MANWON + (tax_base - 8800*MANWON)*0.35
	elif tax_base <= 30000*MANWON:
		return 3760*MANWON + (tax_base - 15000*MANWON)*0.38
	elif tax_base <= 50000*MANWON:
		return 9460*MANWON + (tax_base - 30000*MANWON)*0.4
	elif tax_base > 50000*MANWON:
		return 17460*MANWON + (tax_base - 50000*MANWON)*0.42

#근로소득 세액공제
def calc_earned_income_tax_credit(tax_assessment, salary):
	tax_credit = 0
	if tax_assessment <=50*MANWON:
		tax_credit = tax_assessment*0.55
	else:
		tax_credit = 27.5*MANWON+(tax_assessment-50*MANWON)*0.3
	#간이세액표 상 근로소득공제 한도
	if salary <= 5500*MANWON and tax_credit >= 66*MANWON:
		tax_credit = 66*MANWON
	elif salary <= 7000 and tax_credit >= 63*MANWON:
		tax_credit = 53*MANWON
	elif salary > 7000*MANWON and tax_credit > 50*MANWON:
		tax_credit = 50*MANWON
	return tax_credit

#결정세액
def calc_finalized_tax_amount(tax_base, tax_credit):
	return tax_base-tax_credit

#간이세액
def calc_ease_tax_amount(finalized_tax_amount):
	return round(finalized_tax_amount/12, -1)

number_of_people = 1
# salary = calc_total_annual_income(2505000, 'monthly')
salary = calc_total_annual_income(30000000)
print("연간 총급여액: {}".format(salary))
earned_income_deduction = calc_earned_income_deduction(salary)
print("근로소득공제: {}".format(earned_income_deduction))
earned_income_amount = calc_earned_income_amount(salary, earned_income_deduction)
print("근로소득금액: {}".format(earned_income_amount))
personal_allowance = calc_personal_allowance(number_of_people)
print("인적공제: {}".format(personal_allowance))
annuity_insurance = calc_annuity_insurance_deduction(salary)
print("연금보험료공제: {}".format(annuity_insurance))
special_income_deduction = calc_special_income_deduction(salary, number_of_people)
print("특별 소득공제: {}".format(special_income_deduction))
tax_base = calc_tax_base(earned_income_amount, personal_allowance, annuity_insurance, special_income_deduction)
print("과세표준: {}".format(tax_base))
tax_assessment = calc_tax_assessment(tax_base)
print("산출세액: {}".format(tax_assessment))
tax_credit = calc_earned_income_tax_credit(tax_assessment, salary)
print("근로소득 세액공제: {}".format(tax_credit))
finalized_tax_amount = calc_finalized_tax_amount(tax_assessment, tax_credit)
print("결정세액: {}".format(finalized_tax_amount))
simplicity_tax_amount = calc_ease_tax_amount(finalized_tax_amount)
print("간이세액: {}".format(simplicity_tax_amount))