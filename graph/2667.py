import sys
n=int(sys.stdin.readline())
graph=[]
size_list=[] # 단지 내의 집의 수 담기
count=0 # 단지의 수
for _ in range(n):
    line=sys.stdin.readline()
    line=line[:n]
    line=[int(char) for char in line]
    graph.append(line)
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(y,x):
    global size
    global graph
    if graph[y][x]==0:
        return
    # 방문 처리
    graph[y][x]=0
    size+=1
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or X>n-1 or Y<0 or Y>n-1:
            continue
        if graph[Y][X]==1:
            dfs(Y,X)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            size=0
            dfs(i,j)
            size_list.append(size)
            count+=1
print(count)
size_list.sort()
for i in range(count):
    print(size_list[i])