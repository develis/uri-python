a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (abs(b - c) < a and a < b + c and abs(a-c) < b and b < a + c and abs(a-b) < c and c < a + b):
    if (a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b):
        print('TRIANGULO RETANGULO')
    elif (a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b):
        print('TRIANGULO OBTUSANGULO')
    elif (a*a < b*b + c*c or b*b < a*a + c*c or c*c < a*a + b*b):
        print('TRIANGULO ACUTANGULO')
    if (a == b and b == c):
        print('TRIANGULO EQUILATERO')
    if (a == b and a != c or b == c and b != a or c == a and b != a):
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
