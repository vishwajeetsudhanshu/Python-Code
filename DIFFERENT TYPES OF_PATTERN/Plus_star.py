x=int(input())
for i in range(x):
    for j in range(x):
        if i==x//2 or j ==x//2:
            print("*\t",end="")
        else:
            print(" \t",end="")
    print()
    
    