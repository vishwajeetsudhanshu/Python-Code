x=int(input("enter the values"))
ans=0
while x!=0:
    r=x%10
    x=x//10
    ans=ans*10+r
print(ans)