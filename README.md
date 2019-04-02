# kosimpletax 대한민국 근로 소득 간이 세금 계산

kosimpletax는 [근로소득 간이세액표](https://www.nts.go.kr/support/support_03_etc01.asp)의 내용을 바탕으로 python을 사용하여 개발하였습니다. 연말 정산을 위해 근로 소득 간이 세액을 계산하거나 근로자의 4대 보험 중 근로자가 부담하는 건강보험료, 국민연금료, 고용보험료, 장기요양보험료를 계산할 수 있는 파이썬 패키지입니다. 연봉, 월급에 대해 과세되는 금액을 계산할 수 있습니다. 

> * 원천징수의무자가 매월분의 근로소득을 지급하는 때에는 「소득세법」제134조 및 같은법 시행령 제194조에 따라 근로소득 간이세액표(시행령 별표2)에 의하여 원천징수하도록 규정하고 있습니다.
> * 근로소득 간이세액표는 연말정산시 추가납부 등에 따른 근로자의 부담을 분산하기 위해 월 급여수준과 공제대상 부양가족 수 별로 매월 원천징수해야하는 세액을 정한 표입니다

***계산된 금액은 실제 징수 금액과 차이가 있을 수 있습니다.***

예제 코드:

``` 
    # 연간 총 급여액이 3006만원(비과세 소득과 과세되는 학자금 제외)인 1인가구의 경우
	
	from kosimpletax.y2018 import tax_calculator
	calc = tax_calculator.Calculator()
	result = calc.earned_income_tax(30060000, 'year')
	print(result) # 41630
```

```
	# 월급여액이 500만원인(비과세 소득과 과세되는 학자금 제외)인 근로자의 공제대상 가족의 수가 5명(20세 이하 자녀 3명 포함)인 경우
	
	from kosimpletax.y2018 import tax_calculator
	calc = tax_calculator.Calculator()
	calc.set_family_dependent(5)
	calc.set_less_than_twenty(3)
	result = calc.earned_income_tax(5000000)
	print(result) # 159100
```