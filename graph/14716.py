import sys
sys.setrecursionlimit(100000000)
m, n = map(int, sys.stdin.readline().split())
dx=[0,0,-1,1,-1,-1,1,1]
dy=[1,-1,0,0,1,-1,1,-1]
count=0
def dfs(x,y):
    if graph[y][x]==0:
        return
    graph[y][x]=0 # 방문 처리
    for i in range(8):
        X = x+dx[i]
        Y = y+dy[i]
        if X < 0 or Y < 0 or X > n-1 or Y > m-1:
            continue
        if graph[Y][X] == 1:
            dfs(X, Y)
graph=[]
for _ in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    graph.append(l)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(j,i)
            count += 1
print(count)