import sys
n, m = map(int, sys.stdin.readline().split())
card=[]
max_val=0
for _ in range(n):
    l=list(map(int, sys.stdin.readline().split()))
    if min(l)>max_val:
        max_val=min(l)
print(max_val)