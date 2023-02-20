import copy
import sys
from collections import deque
import heapq
n,m,v = map(int, sys.stdin.readline().split())
visited1=[0]*(n+1) # dfs전용
visited2=[0]*(n+1) # bfs전용
# 그래프 생성
graph1={}
for i in range(n):
    graph1[i+1]=[]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    heapq.heappush(graph1[a], b)
    heapq.heappush(graph1[b], a)
graph2=copy.deepcopy(graph1)

def dfs(recent):
    global visited1
    if visited1[recent]==1:
        return
    # 해당 노드 방문 처리
    visited1[recent]=1
    print(recent, end=" ")

    # 연결되어 있는 다른 노드 방문
    while graph1[recent]:
        v = heapq.heappop(graph1[recent])
        if visited1[v]==0:
            dfs(v)
def bfs(recent):
    global visited2
    queue=deque([recent])
    visited2[recent]=1

    while queue:
        v=queue.popleft()

        print(v, end=" ")
        # 현재 노드와 인접한 노드들 확인
        while graph2[v]:
            i=heapq.heappop(graph2[v])

            # 방문하지 않은 노드일 경우 방문 후보에 넣기
            if visited2[i]==0:
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)