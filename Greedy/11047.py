import sys
n, k = map(int, sys.stdin.readline().split())
value=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    value.append(a)
count=0
for i in range(n-1,-1,-1):
    val=value[i]
    tmp=k//val # tmp는 val의 개수
    k=k%val # 남은 돈
    count+= tmp

print(count)