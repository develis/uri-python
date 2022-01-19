income = float(input())
old_income = income

if income >= 0 and income <= 400:
  income *= 0.15
  percentage = "15 %"
elif income >= 400.01 and income <= 800:
  income *= 0.12
  percentage = "12 %"
elif income >= 800.01 and income <= 1200:
  income *= 0.10
  percentage = "10 %"
elif income >= 1200.01 and income <= 2000:
  income *= 0.07
  percentage = "7 %"
elif income > 2000:
  income *= 0.04
  percentage = "4 %"

print("Novo salario:", "{:.2f}".format(income + old_income))
print("Reajuste ganho:", "{:.2f}".format(income))
print("Em percentual:", percentage)
