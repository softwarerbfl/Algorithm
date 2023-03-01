import sys
s=int(sys.stdin.readline())
n=1
while True:
    N=n*(n+1)/2
    if N>s:
        n=n-1
        break
    else:
        n+=1


print(n)