import sys
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
t.sort(reverse=True)
for i in range(n):
    t[i]=t[i]+i+1
print(max(t)+1)