import sys
sys.setrecursionlimit(10000000)
n, m, k = map(int, sys.stdin.readline().split())
graph=[[0]*m for _ in range(n)]
max_size=0 # 가장 큰 음식물 크기

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(k):
    y,x = map(int, sys.stdin.readline().split())
    graph[y-1][x-1]=1

size = 0
def dfs(y,x):
    global size
    if graph[y][x]==0:
        return
    size += 1
    graph[y][x]=0 # 방문 처리
    for z in range(4):
        X=x+dx[z]
        Y=y+dy[z]
        if X<0 or Y<0 or X>m-1 or Y>n-1:
            continue
        if graph[Y][X]==1:
            dfs(Y,X)
for i in range(n):
    for j in range(m):
        size=0
        if graph[i][j]==1:
            dfs(i,j)
        if size>max_size:
            max_size=size
print(max_size)