x=int(input("enter no:-"))
for i in range(1,x+1):
    if(i==1 or i==x):
        print("*"*x)
    else:
        print("*",end="")
        print(" "*(x-2),end="")
        print("*")