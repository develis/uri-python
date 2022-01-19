def mdc(num1, num2):
  if num1 % num2 == 0:
    return num2
  else:
    return mdc(num2, num1 % num2)

cases = int(input())

for i in range(cases):
  num1, num2 = input().split()
  num1 = int(num1)
  num2 = int(num2)
  print(mdc(num1, num2))
