import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph={i:[] for i in range(1,n+1)}
visit=[0]*(n+1)
q=deque()
for _ in range(m):
    u,v =map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visit[r]=1 # 시작 지점 방문 처리
q.append(r)
count=1 # 방문 순서
while q:
    tmp=graph[q.popleft()] # 방문한 큐와 연결되어 있는 정점들
    tmp.sort(reverse=True)
    for t in tmp:
        # 아직 방문안한 노드인 경우
        if visit[t]==0:
            count+=1
            visit[t]=count # 방문처리
            q.append(t)
for i in range(n):
    print(visit[i+1])
