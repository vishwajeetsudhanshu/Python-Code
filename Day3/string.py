a=input("enter string:")
y=a.lower()
cnt=0
for i in range(0,len(a)):
    if a[i]==y[i]:
        cnt=cnt+1
print(cnt)        