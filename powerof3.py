n=int(input("enter no."))
if n==0:
    print("error")
else:
    for i in range(1,n+1):
        if n%3==0:
            n=n//3
    if(n==1):
     print("true")
    else:
        print("false")