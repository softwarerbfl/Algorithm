import sys
n=int(sys.stdin.readline())

l=[]
for _ in range(n):
    name, d, m, y=sys.stdin.readline().split()
    d, m, y = map(int, [d, m, y])
    l.append([y,m,d,name])

l.sort()
print(l[n-1][3])
print(l[0][3])