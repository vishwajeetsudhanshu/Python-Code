# int=input("enter no:")
def check (n):
    if n==1:
        return True
    if n==0:
        return False
    if n%3!=0:
        return False
    
    return check(n//3)
x=int(input("enter"))
print(check(x))


