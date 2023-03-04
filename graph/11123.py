import sys
sys.setrecursionlimit(100000000)
t=int(sys.stdin.readline())
# 방향 벡터
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,w,h):
    global graph
    # 방문 처리
    if graph[y][x]=='#':
        graph[y][x]='.'
    for i in range(4):
        Y=y+dy[i]
        X=x+dx[i]
        if X<0 or Y<0 or X>=w or Y>=h:
            continue
        else:
            if graph[Y][X]=="#":
                dfs(X,Y,w,h)
for _ in range(t):
    y, x= map(int, sys.stdin.readline().split())
    graph=[]
    count=0
    for _ in range(y):
        l=list(sys.stdin.readline())
        graph.append(l[:len(l)-1])
    for i in range(y):
        for j in range(x):
            if graph[i][j]=='#':
                dfs(j,i,x,y)
                count+=1
            else:
                continue
    print(count)