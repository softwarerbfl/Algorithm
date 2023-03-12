import sys
sys.setrecursionlimit(100000000)
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]
def dfs(x,y):
    global w
    global h
    if graph[y][x]==0:
        return
    # 방문 처리
    graph[y][x]=0
    for i in range(8):
        Y=y+dy[i]
        X=x+dx[i]
        if Y<0 or X<0 or X>w-1 or Y>h-1:
            continue
        if graph[Y][X]==1:
            dfs(X,Y)
while True:
    w, h= map(int, sys.stdin.readline().split())
    count = 0 # 섬의 개수
    if w==0 and h==0 :
        break
    graph=[]
    for _ in range(h):
        island=list(map(int, sys.stdin.readline().split()))
        graph.append(island)
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(j,i)
                count+=1
    print(count)