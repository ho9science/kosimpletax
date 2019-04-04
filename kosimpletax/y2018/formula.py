MANWON = 10000
CHONWON = 1000
def median_income_section(pay):
	str_pay = str(int(pay/10000))
	median = 0
	if pay < 1060*CHONWON:
		median = 0
	elif pay < 1500*CHONWON:		
		if int(int(str_pay)/5) == 0:
			median = float(str_pay+"25")
		else:
			median = float(str_pay+"75")
		median = median * 100
	elif pay < 3000*CHONWON:
		median = float(str_pay+"5")
		median = median * 1000
	elif pay < 10000*CHONWON:
		point = int(str_pay)%20
		if point == 0 or point == 1:
			median = float(str_pay[0:2]+"1")
		elif point == 2 or point == 3:
			median = float(str_pay[0:2]+"3")
		elif point == 4 or point == 5:
			median = float(str_pay[0:2]+"5")
		elif point == 6 or point == 7:
			median = float(str_pay[0:2]+"7")
		elif point == 8 or point == 9:
			median = float(str_pay[0:2]+"9")
		median = median * 10000
	else:
		median = pay
	return median

#월급여액: 소득구간의 중간값
def calc_total_monthly_income(income):
	median = median_income_section(income)
	return median

#연간 총 급여액
def calc_total_annual_income(income):
	temp = income / 12
	median = median_income_section(temp)
	return median * 12

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
def calc_personal_allowance(number_of_people=1, number_of_less_than_twenty=0):
	return (number_of_people+number_of_less_than_twenty) * 150*MANWON

#국민연금 월 보험료
def calc_national_pension(monthly_salary):
	trimmed_salary = monthly_salary - (monthly_salary % 1000)
	pension_share = trimmed_salary*0.045
	return pension_share - pension_share % 10

#연금보험료공제
def calc_annuity_insurance_deduction(salary):
	monthly_salary = salary/12
	annuity_insurance_amount = calc_national_pension(monthly_salary) * 12
	if monthly_salary <= 30*MANWON:
		annuity_insurance_amount = 15.66*MANWON
	elif monthly_salary >= 448*MANWON:
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
	temp_tax_base = 0
	if tax_base <= 1200*MANWON:
		temp_tax_base = tax_base*0.06
	elif tax_base <= 4600*MANWON:
		temp_tax_base = 72*MANWON + (tax_base - 1200*MANWON)*0.15
	elif tax_base <= 8800*MANWON:
		temp_tax_base = 582*MANWON + (tax_base - 4600*MANWON)*0.24
	elif tax_base <= 15000*MANWON:
		temp_tax_base = 1590*MANWON + (tax_base - 8800*MANWON)*0.35
	elif tax_base <= 30000*MANWON:
		temp_tax_base = 3760*MANWON + (tax_base - 15000*MANWON)*0.38
	elif tax_base <= 50000*MANWON:
		temp_tax_base = 9460*MANWON + (tax_base - 30000*MANWON)*0.4
	elif tax_base > 50000*MANWON:
		temp_tax_base = 17460*MANWON + (tax_base - 50000*MANWON)*0.42
	return temp_tax_base - temp_tax_base % 10

#근로소득 세액공제
def calc_earned_income_tax_credit(tax_assessment, salary):
	tax_credit = 0
	if tax_assessment <=50*MANWON:
		tax_credit = tax_assessment*0.55
	else:
		tax_credit = 27.5*MANWON+(tax_assessment-50*MANWON)*0.3
	#간이세액표 상 근로소득공제 한도
	if tax_credit > 66*MANWON:
		if salary <= 5500*MANWON:
			tax_credit = 66*MANWON
		elif salary <= 7000*MANWON:
			tax_credit = 63*MANWON
		elif salary > 7000*MANWON:
			tax_credit = 50*MANWON
	elif tax_credit > 63*MANWON:
		if salary <= 7000*MANWON:
			tax_credit = 63*MANWON
		elif salary > 7000*MANWON:
			tax_credit = 50*MANWON
	elif tax_credit > 50*MANWON:
		if salary > 7000*MANWON:
			tax_credit = 50*MANWON
	return tax_credit - tax_credit % 10

#결정세액
def calc_finalized_tax_amount(tax_base, tax_credit):
	return tax_base-tax_credit

#간이세액
def calc_ease_tax_amount(finalized_tax_amount):
	temp_amount = finalized_tax_amount/12
	return temp_amount - temp_amount % 10

#건강보험
def calc_health_insurance(monthly_salary):
	health_insurance = monthly_salary * 0.0646
	return health_insurance - health_insurance % 10

#장기요양보험료
def calc_long_term_insurance(health_insurance):
	long_term_insurance = health_insurance * 0.0851
	return long_term_insurance - long_term_insurance % 10

#고용보험
def calc_employment_insurance(monthly_salary):
	employment_insurance = monthly_salary * 0.0065
	return employment_insurance - employment_insurance % 10

