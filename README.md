# 근로소득 간이세액표 for python

kosimpletax는 연말정산을 위한 [근로소득 간이세액표](https://www.nts.go.kr/support/support_03_etc01.asp)의 내용을 python으로 코딩하여 근로소득 간이 세액을 계산할 수 있는 파이썬 패키지입니다. 연봉, 월급에 대해 과세되는 금액을 계산할 수 있습니다. 

> * 원천징수의무자가 매월분의 근로소득을 지급하는 때에는 「소득세법」제134조 및 같은법 시행령 제194조에 따라 근로소득 간이세액표(시행령 별표2)에 의하여 원천징수하도록 규정하고 있습니다.
> * 근로소득 간이세액표는 연말정산시 추가납부 등에 따른 근로자의 부담을 분산하기 위해 월 급여수준과 공제대상 부양가족 수 별로 매월 원천징수해야하는 세액을 정한 표입니다

***계산된 금액은 실제 징수 금액과 차이가 있을 수 있습니다.***

예제 코드:

``` 
  from kosimpletax.y2018 import tax_alculator
  calc = tax_calculator.Calculator()
  result = calc.get_simple_tax_amount(25000000)
  print(result)
  
```