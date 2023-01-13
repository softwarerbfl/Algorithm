import sys
import heapq

n=int(sys.stdin.readline())
h=[]
for i in range(n):
    h=h+list(map(int, sys.stdin.readline().split()))
    h=heapq.nlargest(n,h)

print(h[n-1])