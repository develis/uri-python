cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)

if cod == 1:
    print('Total: R$', "{:.2f}".format(qtd * 4.00))
elif cod == 2:
    print('Total: R$', "{:.2f}".format(qtd * 4.50))
elif cod == 3:
    print('Total: R$', "{:.2f}".format(qtd * 5.00))
elif cod == 4:
    print('Total: R$', "{:.2f}".format(qtd * 2.00))
elif cod == 5:
    print('Total: R$', "{:.2f}".format(qtd * 1.50))