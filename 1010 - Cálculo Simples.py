c1, n1, v1 = input().split(" ")
c2, n2, v2 = input().split(" ")
vt = int(n1)*float(v1)+int(n2)*float(v2)
formatted_vt = "{:.2f}".format(vt)
print('VALOR A PAGAR: R$',formatted_vt)


