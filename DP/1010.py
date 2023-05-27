import sys
import math
t=int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    min_num=min(n,m)
    max_num=max(n,m)
    print(int(math.factorial(max_num)/(math.factorial(min_num)*math.factorial(max_num-min_num))))
