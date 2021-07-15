A, B, C = input().split(" ")
t = (float(A)*float(C))/2
ta = "{:.3f}".format(t)
c = 3.14159*float(C)*float(C)
ca = "{:.3f}".format(c)
trap = ((float(A)+float(B))*float(C))/2
trapa = "{:.3f}".format(trap)
q = float(B)*float(B)
qa = "{:.3f}".format(q)
r = float(A)*float(B)
ra = "{:.3f}".format(r)

print('TRIANGULO:', ta)
print('CIRCULO:', ca)
print('TRAPEZIO:', trapa)
print('QUADRADO:', qa)
print('RETANGULO:', ra)


