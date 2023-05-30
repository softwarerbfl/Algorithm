import sys
n=int(sys.stdin.readline())
result=[]
result.append(1)
result.append(1)
if n<=2:
    print(result[n-1])
    exit()
for i in range(1,n):
    result.append(result[i]+result[i-1])
print(result[n-1])