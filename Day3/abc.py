x=input()
for i in x:
  if i>='a' and i<='z':
    print(chr(ord(i)-32),end="")
  else:
    print(chr(ord(i)+32),end="")