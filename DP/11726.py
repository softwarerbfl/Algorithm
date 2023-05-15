import sys
n=int(sys.stdin.readline())
def square(x):
    if num[x]!=0:
        return num[x]
    else:
        num[x]=square(x-1)+square(x-2)
        return num[x]
num=[0 for _ in range(1001)]
num[1]=1
num[2]=2
num[3]=3
num[4]=5
num[5]=8

if num[n]!=0:
    print(num[n])
else:
    print(square(n)%10007)