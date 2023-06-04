import sys
n=int(sys.stdin.readline())
result=[0 for _ in range(1001)]
result[1]=1
result[2]=3
result[3]=5
result[4]=11
result[5]=21
if result[n]!=0:
    print(result[n])
else:
    for i in range(5,n+1):
        result[i]=result[i-1]+result[i-2]*2
    print(result[n]%10007)

