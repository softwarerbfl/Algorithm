import sys
import copy
sys.setrecursionlimit(100000000)
graph_tmp=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
count=0
n=int(sys.stdin.readline())
def dfs(x,y,h):
    global count
    global graph
    if graph[y][x]<=h:
        return
    graph[y][x]=0
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or Y<0 or X>n-1 or Y>n-1:
            continue
        elif graph[Y][X]>h:
            dfs(X,Y,h)

for _ in range(n):
    area=list(map(int, sys.stdin.readline().split()))
    graph_tmp.append(area)

all_area=[] # 비의 양에 따른 안전한 영역의 개수
for h in range(0,101):
    graph=copy.deepcopy(graph_tmp)
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:
                dfs(j, i, h)  # 안전한 영역 찾기
                count+=1
    all_area.append(count)

print(max(all_area))