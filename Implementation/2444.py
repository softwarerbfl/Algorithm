import sys
n=int(sys.stdin.readline())
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n,0,-1):
    print(" "*(n-i+1)+"*"*(2*(i-2)+1))
