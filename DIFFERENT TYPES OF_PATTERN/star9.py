x=int(input("enter no:-"))
for i in range (x+3):
    if i>=x:
        print(" "*(x-1),end="")
        print("*")
    else:
        print(" "*(x-i),end="")
        print("*"*(2*i-1))
    
    