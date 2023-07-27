import sys

x,y,z=map(int, sys.stdin.readline().split())
while x!=0 and y!=0 and z!=0:
    l=[x,y,z]
    l.sort()
    if l[2]**2==l[0]**2+l[1]**2:
        print("right")
    else:
        print("wrong")
    x, y, z= map(int,sys.stdin.readline().split())