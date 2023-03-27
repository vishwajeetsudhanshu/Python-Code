x=int(input("enter the values"))
y=x
ans=0
while x!=0:
    r=x%10
    x=x//10
    ans=ans*10+r
if ans==y:
  print("palindrome no.")
else:
   print("not a palindrome")  