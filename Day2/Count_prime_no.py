def isPrime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False
    

cnt = 0

for i in range(1,10001):
    if isPrime(i):
        cnt += 1
        print(i, end= " ")

print("\n\n Total prime Number is 😍 : ",cnt )