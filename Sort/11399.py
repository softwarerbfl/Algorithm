import sys

n=int(sys.stdin.readline())
p=list(map(int, sys.stdin.readline().split()))
p.sort()

total=0
for i in range(n):
    total+= p[i]*(n-i)
print(total)