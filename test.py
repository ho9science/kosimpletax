from kosimpletax.y2018 import tax_calculator

calc = tax_calculator.calculator()
result = calc.get_simple_tax_amount(25000000)
print(result)