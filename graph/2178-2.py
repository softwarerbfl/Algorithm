import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

graph=[]
move=0 # 이동한 칸 수
for _ in range(n):
    l=list(map(int, input()))
    graph.append(l)

q=deque()
q.append([0, 0])
graph[0][0]=0 # 시작 지점 방문 처리
# BFS
while q:
    l=len(q) # 현재 이동할 수 있는 경우의 가짓수
    move += 1  # 이동
    for i in range(l):
        x, y = q.popleft()
        for j in range(4):
            X=x+dx[j]
            Y=y+dy[j]
            # 영역을 벗어난 경우 SKIP
            if X<0 or Y<0 or X>n-1 or Y>m-1 :
                continue
            # 아직 방문하지 않은 영역인 경우 방문 시작
            if graph[X][Y]==1:
                q.append([X,Y])
                graph[X][Y] = 0 # 방문 처리
    # 도착 지점 도달
    if len(q)==0 or graph[n-1][m-1]==0:
        break
print(move+1)