import sys
sys.setrecursionlimit(10000000)
n=int(sys.stdin.readline())
#a에서 b로 가는 경로가 있는 지 여부를 return
def dfs(a,b):
    global n
    global i
    global stack
    stack.append(a)
    road=graph[a] # a에서 가는 경로들
    # a에서 b로 바로 가는 경로가 있는 경우
    if graph[a][b]==1:
        graph[i][b]=1
        return
    # 바로 가는 경우가 없는 경우 가능한 길 타고 가보기
    for k in range(n):
        if road[k] == 1 and k not in stack:
            dfs(k,b)
        if graph[i][b]==1: # 길을 찾아보다가 찾은 경우 아예 종료
            return
    return

graph={i : None for i in range(n)}
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    graph[i] = l

for i in range(n):
    for j in range(n):
        # i에서 j로 바로 가는 경우가 없는 경우에만 dfs
        if graph[i][j]==0:
            stack=[]
            dfs(i,j)
    print(" ".join(map(str,graph[i])))
