a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

AB = (a+b+abs(a-b))/2;
AC = (a+c+abs(a-c))/2;
BC = (b+c+abs(b-c))/2;

if AB >= AC and AB >= BC:
    print("%d"%(AB), 'eh o maior')
elif AC >= AB and AC >= BC:
    print("%d"%(AC), 'eh o maior' )
else:
    print("%d"%(BC), 'eh o maior' )




