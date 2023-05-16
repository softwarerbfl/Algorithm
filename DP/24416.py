import sys
n=int(sys.stdin.readline())
num=[0 for _ in range(41)]
num[1]=1
num[2]=1
count=0

for i in range(3,n+1):
    num[i]=num[i-1]+num[i-2]


print(num[n],n-2)