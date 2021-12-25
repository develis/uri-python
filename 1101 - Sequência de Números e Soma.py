flag = 0
while flag != 1:
    m, n = input().split()
    m = int(m)
    n = int(n)
    if (n <= 0 or m <= 0):
        flag = 1
    if m > n:
        som = 0
        if flag != 1:
            for i in range(n, m+1):
                print('%d '%(i),end="")
                som += i
    if n > m:
        som = 0
        if flag != 1:
            for i in range(m, n+1):
                print(i, '')
                som += i
    if flag != 1: print('Sum=%d'%(som))
