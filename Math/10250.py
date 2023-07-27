import sys
t=int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    num=n//h+1
    floor = n%h
    if n%h==0:
        num=n//h
        floor = h
    print(str(floor)+str(num).zfill(2))