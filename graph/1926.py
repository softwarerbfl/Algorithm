import sys
sys.setrecursionlimit(100000000)
n,m = map(int, sys.stdin.readline().split())
graph = [] # 도화지
count=0
max_size=0
size=0
# 좌우하상
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    line=list(map(int, sys.stdin.readline().split()))
    graph.append(line[:m])
def dfs(y,x):
    global graph
    global size
    if graph[y][x]==0:
        return
    # 방문 처리
    graph[y][x]=0
    size+=1
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or X>m-1 or Y<0 or Y>n-1:
            continue
        # 아직 방문을 안했을 경우에만 방문
        if graph[Y][X]==1:
            dfs(Y,X)
for i in range(n):
    for j in range(m):
        # 아직 방문하지 않았다면 탐색 시작
        if graph[i][j]==1:
            size=0
            dfs(i,j)
            # 만약 그림의 넓이가 최대 크기라면
            if size>max_size:
                max_size=size
            count+=1 # 개수 증가
print(count)
print(max_size)