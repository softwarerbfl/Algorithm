import sys
sys.setrecursionlimit(100000000)
m, n, k = map(int, sys.stdin.readline().split())
graph=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
size=0
all_size=[]
def dfs(x,y):
    global size
    if graph[x][y]==1:
        return
    # 방문 처리
    graph[x][y]=1
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or Y<0 or X>m-1 or Y>n-1:
            continue
        else:
            if graph[X][Y]==0:
                dfs(X,Y)
                size+=1

for _ in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x]=1
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            size=1
            dfs(i,j)
            all_size.append(size)

print(len(all_size))
all_size.sort()
print(" ".join(map(str, all_size)))