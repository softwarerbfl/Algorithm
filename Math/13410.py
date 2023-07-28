import sys

n, k = map(int, sys.stdin.readline().split())
mul = []
for i in range(1, k + 1):
    mul.append(int(str(n * i)[::-1]))

print(max(mul))