def fn(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)
print(fn(8))