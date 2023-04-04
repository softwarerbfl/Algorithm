import sys
sys.setrecursionlimit(100000000)
graph=[]
case=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def dfs(y,x,tmp):
    global case
    # 길이가 6이고 없는 케이스인 경우
    if len(tmp)==6:
        if tmp not in case:
            case.append(tmp)
        return
    for k in range(4):
        X=x+dx[k]
        Y=y+dy[k]
        if X<0 or X>4 or Y<0 or Y>4:
            continue
        if len(tmp)<=5:
            dfs(Y, X, tmp+graph[Y][X])
for _ in range(5):
    l = list(map(str, sys.stdin.readline().split()))
    graph.append(l)
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(case))