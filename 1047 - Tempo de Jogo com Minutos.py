horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial = int(horaInicial)
horaFinal = int(horaFinal)
minutoInicial = int(minutoInicial)
minutoFinal = int(minutoFinal)

mi = (horaInicial*60) + minutoInicial
mf = (horaFinal*60) + minutoFinal

if (mf <= mi): 
    mf += 1440
print('O JOGO DUROU', ((mf-mi)//60), 'HORA(S) E', (mf-mi)%60, 'MINUTO(S)')
