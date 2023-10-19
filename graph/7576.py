import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
    t=list(map(int, sys.stdin.readline().split()))
    box.append(t)
result=0
queue=deque()
# 좌표들을 queue에 넣어줌
for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 영역안에 있고, 그 좌표에 토마토가 익지않은 상태로 있는 경우에 +1해주기
            if 0<= nx< n and 0<=ny<m and box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                queue.append([nx, ny])

bfs()
for i in box:
    for j in i:
        # 안익은 토마토가 존재하면 -1 출력하고 종료
        if j==0:
            print(-1)
            exit(0)
    result=max(result, max(i))
print(result-1)