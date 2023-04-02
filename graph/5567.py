import sys
n=int(sys.stdin.readline()) # 동기의 수
m=int(sys.stdin.readline()) # 리스트의 길이
friend={i : [] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)
visit=set(friend[1])
for i in range(len(friend[1])):
    tmp=set(friend[friend[1][i]])
    visit=visit.union(tmp)
if 1 in visit:
    print(len(visit)-1)
else:
    print(len(visit))
