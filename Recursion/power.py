# int=input("enter no:")
def check (n):
    if n==1:
        return True
    if n==0:
        return False
    if n%2!=0:
        return False
    
    return check(n//2)
x=int(input("enter"))
print(check(x))


