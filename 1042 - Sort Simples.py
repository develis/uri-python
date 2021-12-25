a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (a < b and b < c and a < c):
    print(a)
    print(b)
    print(c)

if (a < b and c < b and a < c):
    print(a)
    print(c)
    print(b)

if (b < a and b < c and a < c):
    print(b)
    print(a)
    print(c)

if (b < a and b < c and c < a):
    print(b)
    print(c)
    print(a)

if (c < a and c < b and a < b):
    print(c)
    print(a)
    print(b)

if (c < a and c < b and b < a):
    print(c)
    print(b)
    print(a)

print()

print(a)
print(b)
print(c)
