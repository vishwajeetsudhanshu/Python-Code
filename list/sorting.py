x=[2,1,2,1,3,4,3]
n=len(x)
x.sort()
i=0
while (i<(n-1)):
    if x[i]==x[i+1]: 
        i=i+2
    else:
        print(x[i])
        break
if i==n-1:
    print(x[i])


