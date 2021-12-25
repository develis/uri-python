a, b = input().split()
a = float(a)
b = float(b)
print("{:.2f}%".format((100*(b-a))/a))