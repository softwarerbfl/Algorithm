import sys

T=int(input())
data=[]
for i in range(T):
    data.append(list(map(int, sys.stdin.readline().split())))
for i in range(T):
    print("Case #{0}: {1}".format(i+1,data[i][0]+data[i][1]))