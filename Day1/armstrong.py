x=int(input("enter the values"))
y=x
t=x
ans=0
count=0
while x!=0:
    x=x//10
    count=count+1
while y!=0:
    r=y%10
    ans=ans+r**count
    y=y//10
if  ans==t:
    print("Armstrong No.") 
else:
    print("not a armstrong") 
  
