# int=input("enter no:")
def check (n):
    if n==1:
        return True
    if n==0:
        return False
    if n%4!=0:
        return False
    
    return check(n//4)
x=int(input("enter"))
print(check(x))


