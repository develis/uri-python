n = float(input())

print('NOTAS:')
print(int(n/100), 'nota(s) de R$ 100.00')
aux = n%100
print(int(aux/50), 'nota(s) de R$ 50.00')
aux = aux%50
print(int(aux/20), 'nota(s) de R$ 20.00')
aux = aux%20
print(int(aux/10), 'nota(s) de R$ 10.00')
aux = aux%10
print(int(aux/5), 'nota(s) de R$ 5.00')
aux = aux%5
print(int(aux/2), 'nota(s) de R$ 2.00')

print('MOEDAS:')
print(int(aux%2), "moeda(s) de R$ 1.00")
aux = (n*100)%100
print(int(aux/50), "moeda(s) de R$ 0.50")
aux = aux%50
print(int(aux/25), "moeda(s) de R$ 0.25")
aux = aux%25
print(int(aux/10), "moeda(s) de R$ 0.10")
aux = aux%10
print(int(aux/5), "moeda(s) de R$ 0.05")
aux = aux%5
print(int(aux), "moeda(s) de R$ 0.01")