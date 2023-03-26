import sys
sys.setrecursionlimit(10000000)
n, m, k = map(int, sys.stdin.readline().split())
graph=[[0]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(y,x):
    global count
    if graph[y][x]==0:
        return
    graph[y][x]=0 # 방문 처리
    count+=1
    for z in range(4):
        X=x+dx[z]
        Y=y+dy[z]
        if X<0 or Y<0 or X>m-1 or Y>n-1:
            continue
        if graph[Y][X]==1:
            dfs(Y,X)
for _ in range(k):
    r, c= map(int, sys.stdin.readline().split())
    graph[r-1][c-1]=1
max_count=0
for i in range(n):
    for j in range(m):
        # 쓰레기 찾았을 경우 탐색 시작
        if graph[i][j]==1:
            count=0
            dfs(i,j)
            if count>max_count:
                max_count=count
print(max_count)