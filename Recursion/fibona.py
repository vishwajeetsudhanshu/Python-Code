n=int(input())

a = 0
b = 1

if(n==1):
    print(a)
elif(n==2):
    print(b)
else:
    print(a,b,end=" ")
    while(n-2>0):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
        n-=1