import sys
sys.setrecursionlimit(100000000)
n, m = map(int, sys.stdin.readline().split())
graph={i:[] for i in range(1,n+1)}
def dfs(v):
    if tmp_visit[v]==1:
        return
    tmp_visit[v]=1 #방문처리
    connect=graph[v] #v번을 신뢰하는 컴퓨터들
    for n in connect:
        if tmp_visit[n] ==1:
            continue
        else:
            dfs(n)
for _ in range(m):
    a, b= map(int, sys.stdin.readline().split())
    graph[b].append(a) # b번에는 b를 신뢰하는 번호들
tmp_visit=[0]*(n+1) # 한 바퀴도는 동안 방문한 노드를 세는 용도
max_count=0
result=[]
for i in range(1, n+1):
    # 방문했거나 해당 노드를 신뢰하는 컴퓨터가 없는 경우
    if len(graph[i])==0:
        continue
    dfs(i)
    count = sum(tmp_visit)  # 해킹한 컴퓨터 개수
    result.append(count)
    tmp_visit = [0] * (n + 1)
max_val=max(result)
for i in range(len(result)):
    if result[i]==max_val:
        print(i+1,end=" ")