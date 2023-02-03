import sys
n,m=map(int, sys.stdin.readline().split())
not_listen=set()
not_see=set()
for i in range(n):
    not_listen.add(sys.stdin.readline().rstrip())

for j in range(m):
    not_see.add(sys.stdin.readline().rstrip())
result=sorted(list(not_see & not_listen))
print(len(result))
for n in range(len(result)):
    print(result[n])