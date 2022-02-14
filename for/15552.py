import sys
T=int(sys.stdin.readline())
a=[]
for i in range(0,T):
    a.append(list(map(int, sys.stdin.readline().split())))
for j in range(0,T):
    print(a[j][0]+a[j][1])