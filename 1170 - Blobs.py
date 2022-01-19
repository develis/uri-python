cases = int(input())
dia = 0

for i in range(cases):
  food = float(input())
  while (food > 1):
    food /= 2
    dia += 1
  print(dia, "dias")
  dia = 0
