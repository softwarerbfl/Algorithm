a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if c - b <= 0:
    i = -1
    print(i)
else:
    i=int(a/(c-b)) +1
    print(i)