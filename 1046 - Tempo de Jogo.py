inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)

if inicio >= fim:
    print('O JOGO DUROU', (24-inicio)+fim, 'HORA(S)')
else:
    print('O JOGO DUROU', fim-inicio, 'HORA(S)')
