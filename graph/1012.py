import sys
sys.setrecursionlimit(100000000)
t=int(sys.stdin.readline())
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(x,y):
    if graph[y][x]==0:
        return
    # 방문 처리
    graph[y][x]=0
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or X>m-1 or Y<0 or Y>n-1:
            continue
        if graph[Y][X]==1:
            dfs(X,Y)
for _ in range(t):
    count=0
    m, n, k = map(int, sys.stdin.readline().split())
    # 배추밭
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x]=1 # 배추 심기

    for i in range(n):
        for j in range(m):
            # 배추가 심어져 있으면 탐색 시작
            if graph[i][j]==1:
                dfs(j,i)
                count+=1
    print(count)

