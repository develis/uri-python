n = int(input())

n100 = n//100
aux = n%100
n50 = aux//50
aux = aux%50
n20 = aux//20
aux = aux%20
n10 = aux//10
aux = aux%10
n5 = aux//5
aux = aux%5
n2 = aux//2
n1 = aux%2

print(n)
print(n100, 'nota(s) de R$ 100,00')
print(n50, 'nota(s) de R$ 50,00')
print(n20, 'nota(s) de R$ 20,00')
print(n10, 'nota(s) de R$ 10,00')
print(n5, 'nota(s) de R$ 5,00')
print(n2, 'nota(s) de R$ 2,00')
print(n1, 'nota(s) de R$ 1,00')

