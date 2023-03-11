import sys
import copy
sys.setrecursionlimit(100000000)
patient=0
normal=0
graph=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
n=int(sys.stdin.readline())
for _ in range(n):
    l=sys.stdin.readline().split()
    l=list(str(l[0]))
    graph.append(l)
visit=[[0]*n for _ in range(n)]
# 환자의 RED, GREEN 지역 카운트
def dfs_rg(y,x):
    global graph
    global visit
    # 파랑색이거나 해당 구역을 이미 방문한 경우
    if graph[y][x]=='B' or visit[y][x]==1:
        return
    # 방문 처리
    visit[y][x]=1
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or X>n-1 or Y<0 or Y>n-1:
            continue
        # 인접 구역이 R이나 G이고 아직 방문을 안한 경우
        if (graph[Y][X]=='G' or graph[Y][X]=='R') and visit[Y][X]==0:
            dfs_rg(Y,X)
def dfs_b(y,x):
    global visit
    global graph
    if graph[y][x]!='B' or visit[y][x]==1:
        return
    # Blue 구역 방문 처리
    visit[y][x]=1
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X > n - 1 or Y < 0 or Y > n - 1:
            continue
        if graph[Y][X]=='B':
            dfs_b(Y,X)
def dfs_r(y,x):
    global visit
    global graph
    if graph[y][x] != 'R' or visit[y][x] == 1:
        return
    # Blue 구역 방문 처리
    visit[y][x] = 1
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X > n - 1 or Y < 0 or Y > n - 1:
            continue
        if graph[Y][X] == 'R':
            dfs_r(Y, X)
def dfs_g(y,x):
    global visit
    global graph
    if graph[y][x] != 'G' or visit[y][x] == 1:
        return
    # Blue 구역 방문 처리
    visit[y][x] = 1
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X > n - 1 or Y < 0 or Y > n - 1:
            continue
        if graph[Y][X] == 'G':
            dfs_g(Y, X)
# 환자 기준의 빨강 초록 파랑 구역 찾기
for i in range(n):
    for j in range(n):
        if (graph[i][j]=='R' or graph[i][j]=='G') and visit[i][j]==0:
            patient+=1
            dfs_rg(i,j)
        elif (graph[i][j]=='B') and visit[i][j]==0:
            patient+=1
            normal+=1
            dfs_b(i,j)
visit=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R' and visit[i][j]==0:
            dfs_r(i,j)
            normal+=1
        elif graph[i][j]=='G' and visit[i][j]==0:
            normal+=1
            dfs_g(i,j)
print(normal,patient)