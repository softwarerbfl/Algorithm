import sys

n,m = map(int, sys.stdin.readline().split(":"))
x=min([min([n, m]),abs(n-m)])

for i in range(x, 0,-1):
    if n%i==0 and m%i==0:
        n=n/i
        m=m/i
        break
print(":".join(map(str,[int(n),int(m)])))