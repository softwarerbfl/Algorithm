import sys
n,m =map(int, sys.stdin.readline().split())
graph={i :[] for i in range(1,n+1)}
visited=[0]*(n+1)
sys.setrecursionlimit(100000000)
for _ in range(m):
    u,v=map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(key):
    global graph
    if visited[key]==1:
        return
    # 방문 처리
    visited[key]=1
    # 현재 정점과 연결되어 있는 노드 불러오기
    connect=graph[key]
    for i in connect:
        if visited[i]==0:
            dfs(i)
    return

count=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        count+=1
print(count)